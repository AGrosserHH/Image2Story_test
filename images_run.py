#https://falahgs.medium.com/convert-any-image-into-short-story-deb4e2f57bcd
from image2caption import *
download_blip()
model_download()

API_KEY=''
file1 = open("./results.txt","a")

image_path='./example.jpg'
caption = image_caption(image_path)
file1.write(caption+"\n")

prompt=caption
short_story=english_story(prompt,API_KEY)
short_story=short_story.replace('.','\n')
file1.write('short story \n')
file1.write(short_story+"\n")

# due to possible copyright not included
#image_path='./example1.jpg'
#caption = image_caption(image_path)
#file1.write(caption+"\n")

#prompt=caption
#short_story=english_story(prompt,API_KEY)
#short_story=short_story.replace('.','\n')
#file1.write(short_story+"\n")

file1.close()
