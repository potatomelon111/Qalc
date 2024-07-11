import quran_data


# Function to calculate total words memorized in given ranges
def calculate_words_memorized(memorized_ranges: list[str]) -> tuple[int, int]:
    total_memorized_words = 0
    total_quran_words = sum(quran_data.WORD_COUNTS.values())

    for range_input in memorized_ranges:
        if ":" not in range_input:
            total_ayahs = len(
                [
                    x
                    for x in quran_data.WORD_COUNTS.keys()
                    if int(x.split(":")[0]) == int(range_input)
                ]
            )
            range_input = f"{range_input}:0-{total_ayahs}"

        surah, ayah_range = [str(x) for x in range_input.split(":")]
        surah_num = int(surah)

        start_ayah, end_ayah = [int(x) for x in ayah_range.split("-")]

        for ayah_num in range(start_ayah, end_ayah + 1):
            ayah_key = f"{surah_num}:{ayah_num}"
            if ayah_key in quran_data.WORD_COUNTS:
                total_memorized_words += quran_data.WORD_COUNTS[ayah_key]

    return total_memorized_words, total_quran_words


# Input the memorized ranges
def input_memorized_ranges() -> list[str]:
    memorized_ranges = input("Enter memorized Ayah: ")
    memorized_ranges = memorized_ranges.split(",")
    return memorized_ranges


# Get user input for memorized ranges
memorized_ranges = input_memorized_ranges()

# Calculate total words memorized and percentage of Quran memorized
memorized, total_quran = calculate_words_memorized(memorized_ranges)
percentage_memorized = (memorized / total_quran) * 100

# Output results
print(f"Total words memorized: {memorized:,d}")
print(f"Total words in the Quran: {total_quran:,d}")
print(f"Percentage of the Quran memorized: {percentage_memorized:.2f}%")
