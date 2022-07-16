from text_generator import RandomText
from compressor import HuffmanCompressor
from compression_rate import compute_kl_distance, compute_space_saving_ratio

if __name__ == "__main__":
    text_model_A = {
        "C": 10,
        "H": 23,
        "L": 12,
        "O": 47,
        "E": 8
    }
    text_model_B = {
        "C": 33,
        "H": 15,
        "L": 7,
        "O": 21,
        "E": 24
    }
    text_length = 50
    print("Text models in percent probability")
    print("Text model A ", text_model_A)
    print("Text model B ", text_model_B)
    print()
    print("Randomly generate TA and TB")
    text_A = RandomText.generate_text(text_model_A, length= text_length)
    text_B = RandomText.generate_text(text_model_B, length= text_length)
    print("TA: ",text_A)
    print("TB: ",text_B)
    print()
    print("Generate code words")  
    compressor_A = HuffmanCompressor(text_model_A)
    compressor_A.generate_code_word_table()
    print("Code words A: ", compressor_A.code_word_table)
    compressor_B = HuffmanCompressor(text_model_B)
    compressor_B.generate_code_word_table()
    print("Code words B: ", compressor_B.code_word_table)
    print()
    print("Compress TA with compressor A and B")
    text_A_compressed_with_A = compressor_A.compress_text(text_A)
    AA_comp_ratio, AA_ori_size, AA_comp_size = compute_space_saving_ratio(text_A, text_A_compressed_with_A)
    text_A_compressed_with_B = compressor_B.compress_text(text_A)
    AB_comp_ratio, AB_ori_size, AB_comp_size = compute_space_saving_ratio(text_A, text_A_compressed_with_B)
    print("TA compressed with CA: ", text_A_compressed_with_A)
    print("Compression ratio: ", AA_comp_ratio, "( ", AA_comp_size, "/", AA_ori_size," bits )")
    print("TA compressed with CB: ", text_A_compressed_with_B)
    print("Compression ratio: ", AB_comp_ratio, "( ", AB_comp_size, "/", AB_ori_size," bits )")
    print()
    print("Compress TB with compressor A and B")
    text_B_compressed_with_A = compressor_A.compress_text(text_B)
    BA_comp_ratio, BA_ori_size, BA_comp_size = compute_space_saving_ratio(text_B, text_B_compressed_with_A)
    text_B_compressed_with_B = compressor_B.compress_text(text_B)
    BB_comp_ratio, BB_ori_size, BB_comp_size = compute_space_saving_ratio(text_B, text_B_compressed_with_B)
    print("TB compressed with CA: ", text_B_compressed_with_A)
    print("Compression ratio: ", BA_comp_ratio, "( ", BA_comp_size, "/", BA_ori_size," bits )")
    print("TB compressed with CB: ", text_B_compressed_with_B)
    print("Compression ratio: ", BB_comp_ratio, "( ", BB_comp_size, "/", BB_ori_size," bits )")
    print()
    print("Relative entropy (KL-distance)")
    compression_rate_text_A_with_A = compute_kl_distance(text_model_A, text_model_A)
    compression_rate_text_A_with_A_bits = compute_kl_distance(text_model_A, text_model_A, bits= True) 
    compression_rate_text_A_with_B = compute_kl_distance(text_model_B, text_model_A)
    compression_rate_text_A_with_B_bits = compute_kl_distance(text_model_B, text_model_A, bits= True)
    print("TA compressed with CA: ", compression_rate_text_A_with_A, " nats ", "( ",compression_rate_text_A_with_A_bits," bits )")
    print("TA compressed with CB: ", compression_rate_text_A_with_B, " nats ", "( ",compression_rate_text_A_with_B_bits," bits )")
    compression_rate_text_B_with_A = compute_kl_distance(text_model_A, text_model_B)
    compression_rate_text_B_with_A_bits = compute_kl_distance(text_model_A, text_model_B, bits=True)
    compression_rate_text_B_with_B = compute_kl_distance(text_model_B, text_model_B)
    compression_rate_text_B_with_B_bits = compute_kl_distance(text_model_B, text_model_B, bits= True)
    print("TB compressed with CA: ", compression_rate_text_B_with_A, " nats ", "( ",compression_rate_text_B_with_A_bits," bits )")
    print("TB compressed with CB: ", compression_rate_text_B_with_B, " nats ", "( ",compression_rate_text_B_with_B_bits," bits )")
    print()
    