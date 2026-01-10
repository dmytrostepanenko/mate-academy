def color_stones(stones: str) -> int:
    # write your code here
    if len(stones) > 0:
        stones_list = []
        for letter in stones:
            stones_list.append(letter)

        index = 0
        result_list = [stones_list[index]]
        for letter in stones_list:
            while result_list[index] != letter:
                result_list.append(letter)
                index += 1
        
        return len(stones_list) - len(result_list)
    else:
        return 0



if __name__ == "__main__":
    print(color_stones("RRGB")) # 1, "R" потрібно прибрати; в результаті залишиться "RGB"
    print(color_stones("RRGGB")) # 2, "R" і "G" потрібно прибрати; в результаті залишиться "RGB"
    print(color_stones("RRRRGB")) # 3, "RRR" потрібно прибрати; в результаті залишиться "RGB"
    print(color_stones("RGBRGBRGGB")) # 1, "G" потрібно прибрати в результаті залишиться "RGBRGBRGB"
    print(color_stones("RGGRGBBRGRR")) # 3, "G", "B" і "R" потрібно прибрати; в результаті   залишиться "RGRGBRGR"
    print(color_stones("RRRRGGGGBBBB")) # 9, "RRR", "GGG" і "BBB" потрібно прибрати; в результаті залишиться "RGB"