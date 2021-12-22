from pytube import YouTube

link = input("Enter the link: ") # ask user for yt video to download
yt = YouTube(link) # pass user's link to YouTube class

# Reveal info about the video
# Title
print("Title: ", yt.title)
# No. of views
print("Number of views: ", yt.views)
# Length of video
print("Length of video: ", yt.length,"seconds")
# Description of video
print("Description: ", yt.description)
# Rating
print("Ratings: ", yt.rating)

# Obtain highest resolution possible
yt = yt.streams.get_highest_resolution()

#start download
print("Downloading...")
#will download mp4
yt.download()
print("Download Complete!")
