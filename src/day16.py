from math import prod
from pathlib import Path

class BitStream:
    'Deliver integers from a stream of bits created from a hexadecimal string'

    bit_str: str
    pos: int

    def __init__(self, hex_nibbles_str: str) -> None:
        def binary_nibble_str(hex_nibble_str: str) -> str:
            'Convert, for example, `e` ➜ `1110`, or `0` ➜ `0000`'
            nibble = int(hex_nibble_str, 16)
            bits_str = bin(nibble)[2:]  # Removes the 0b at the left
            padding_needed = 4 - len(bits_str)
            return '0' * padding_needed + bits_str

        self.bit_str = ''.join(binary_nibble_str(hex_nibble_str)
                               for hex_nibble_str in hex_nibbles_str)
        self.pos = 0

    def next_int(self, num_bits: int) -> int:
        'Get the next `num_bits` bits and return them parsed as a binary number'

        return int(self._next_str(num_bits), 2)

    def _next_str(self, num_bits) -> str:
        'Return the next `num_bits` bits as a string'

        bits_str = self.bit_str[:num_bits]
        self.bit_str = self.bit_str[num_bits:]
        self.pos += num_bits
        return bits_str

class Decoder:
    'Decode the BITS packet and its nested contained packets'

    bits: BitStream
    versions_sum: int

    operators = [
        sum, prod, min, max, None,
        lambda vals: int(vals[0] > vals[1]),
        lambda vals: int(vals[0] < vals[1]),
        lambda vals: int(vals[0] == vals[1]),
    ]

    def __init__(self, packet_hex):
        self.bits = BitStream(packet_hex)
        print(f'Decoder started for {len(self.bits.bit_str)} bits {packet_hex} {self.bits.bit_str}')
        self.versions_sum = 0

    def parse(self, level=0) -> int:
        def parse_literal() -> int:
            value = 0
            more: bool = True
            while more:
                more = bool(next_int(1))
                nibble: int = next_int(4)
                value = (value << 4) + nibble  # Slide over and drop in new bits
            print(f'{value=}')
            return value

        def parse_operator(type: int) -> int:
            def parse_subpackets_by_length(packets_length) -> list[int]:
                values: list[int] = []
                print(f'{packets_length=}')
                stop_pos = self.bits.pos + packets_length
                while self.bits.pos < stop_pos:
                    values.append(self.parse(level + 1))
                return values

            def parse_subpackets_by_count(packet_count) -> list[int]:
                print(f'{packet_count=}')
                return [self.parse(level + 1) for _ in range(packet_count)]

            subpacket_parsers = [parse_subpackets_by_length, parse_subpackets_by_count]
            length_type_id = next_int(1)
            length_or_count = next_int(15 if length_type_id == 0 else 11)
            values = subpacket_parsers[length_type_id](length_or_count)
            return Decoder.operators[type](values)

        next_int = self.bits.next_int
        indent = '  ' * level
        ver = next_int(3)
        self.versions_sum += ver
        type = next_int(3)
        print(indent + f'{ver=}, {type=}, ', end='')
        return parse_literal() if type == 4 else parse_operator(type)

if __name__ == '__main__':
    decoder = Decoder(Path('../data/16.txt').read_text().strip())
    print(f'Result: {decoder.parse()}, versions sum: {decoder.versions_sum}')
