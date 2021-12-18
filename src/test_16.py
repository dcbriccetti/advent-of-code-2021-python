from unittest import TestCase
from day16 import BitStream, Decoder


class TestBitStream(TestCase):
    def test_correct_value_are_streamed(self):
        bits = BitStream('01ef')
        expected_values = [0, 1, 14, 15]
        for expected_value in expected_values:
            self.assertEqual(expected_value, bits.next_int(4))

class TestDecoder(TestCase):
    def test_version_numbers_sum_correctly(self):
        test_data_pairs = [
            ('D2FE28', 6),
            ('38006F45291200', 9),
            ('EE00D40C823060', 14),
            ('8A004A801A8002F478', 16),
            ('620080001611562C8802118E34', 12),
            ('C0015000016115A2E0802F182340', 23),
            ('A0016C880162017C3686B18A3D4780', 31)
        ]
        for test_data_pair in test_data_pairs:
            hex_str = test_data_pair[0]
            decoder = Decoder(hex_str)
            decoder.parse(0)
            versions_sum = decoder.versions_sum
            print(f'{versions_sum=}')
            self.assertEqual(test_data_pair[1], versions_sum)

    def test_operations(self):
        test_data_pairs = [
            ('C200B40A82', 3),
            ('04005AC33890', 54),
            ('880086C3E88112', 7),
            ('CE00C43D881120', 9),
            ('D8005AC2A8F0', 1),
            ('F600BC2D8F', 0),
            ('9C005AC2F8F0', 0),
            ('9C0141080250320F1802104A08', 1),
        ]
        for test_data_pair in test_data_pairs:
            hex_str = test_data_pair[0]
            decoder = Decoder(hex_str)
            self.assertEqual(test_data_pair[1], decoder.parse())
