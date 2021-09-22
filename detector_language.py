from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

text='an indian tale'
idiom=detect(text)

print(text, idiom)