from youtubeStatstics import YTStats

# Youtube v3 API from https://console.cloud.google.com/apis
API_KEY = "AIzaSyB7VRys9vS2-3tMmMWrSGkzaZheGu_ZW4w"

# Function for processing the youtube video with channel id as a parameter
def processingTheVid(channelId):
    # Getting the channel id from https://commentpicker.com/youtube-channel-id.php 
    # Currently using the Carryminati's youtube channel id
    # channelId = "UCclJ1kaHxEC5P-VDZ_BsuJA"

    print(channelId)

    # Creating a YTStats object named youtube
    youtube = YTStats(API_KEY, channelId)
    # Executing the getChannelStats method of YTStats object
    youtube.getChannelStats()
    # Executing the getChannelVideoData method of YTStats object
    youtube.getChannelVideoData()
    # Dumping or Writing the youtube object json text data in a file named channel name with extension of json file
    youtube.dumpJSON()