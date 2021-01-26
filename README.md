# instagram-media-organizer

This Python script assists in organizing downloaded media content from Instagram profiles which were downloaded by using **Chrome Extension** called **Downloader for Instagram.**

That Chrome Extension by default stores all downloaded media from Instagram in **Downloads** directory. This script extracts instagram profile username from media file's name,
and stores it in **Downloads\profiles\username\** folder.

## Example of it's function:
Let's say there's a file called **yurigameplays_88856306_314113863211478_6833272711372430623_n.mp4** in **Downloads** folder.
Now this python script creates folder called **yurigameplays** in **Downloads\profiles\** folder and stores that media file in there.

Basically it's organizing files. The reason why I made it is because once you download too many files from Instagram, 
they all get messy, and is tiresome to manually organize them.

## Note:
This will probably be useful to you only if you have such files in Downloads folder, and also with same filename formatting *(username_number_number_number_n.***)*

I would advise using **Downloader for Instagram** extension.
Since I cannot seem to find this extension on Chrome Web Store, here is an [alternative link](https://www.crx4chrome.com/crx/86579/).
