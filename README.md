# ㅤقalc
ㅤقalc (or Qalc for the places where I don't have unicode) is short for Quran Calcultor, and is a program to calculate a decently accurate estimate for the percentage of Quran you have memorised. It uses a word by word bases rather than verse, which rewards accordingly whether a long verse or short verse has been memorised (in terms of percentage, but of course there is more reward that a program can not show...)
**This program gives an approximate estimate, as the total word count may differ based on the methodolgy used to count it**
# TODO
- [ ] implement juz-based input (e.g. #30 adds the whole of juz 30)
- [ ] add the ability to add a range of Surah if learned in order
- [ ] add memory
# Usage
- begin by pasting `git clone https://github.com/potatomelon111/Qalc/` in the terminal followed by `cd ~/Qalc` (or if you're on linux, figure it out yourself)
- ensure python3 is installed however you see fit (I am familliar with, so like to use the scoop package manager on windows)
- now run the command `python qc.py` (which tells python to run the program)
- now you can input the verses you know in the standard format of `1:1-7` (first chapter, verse 1 to 7) and repeat this for any range of verses, seperate the ranges with a comma, not a space like so: `1:1-7,114:1-6,112:1-3` etc. (Note, if you know the entire chapter/surah, you can just put the surah number followed by a comma, nothing else)
- hit enter to have your result, small percentage? Don't be disheartened keep on working hard, everyone was there at one point! Large percentage? Well done, keep going!

To any programmers reading the code, sorry!
