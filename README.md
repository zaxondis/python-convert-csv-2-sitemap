python-convert-csv-2-sitemap
========================

This simple script will read all CSV files in a directory and convert them to a Sitemap.

HOW TO USE THE FILE:

1. Change the 'path' variable (line 10) to your directory. The example is using Windows path declaration, if you're
  using Linux be sure to delcare the path properly for your operating system.

2. Change the the first string in the  'smf' variable to any file name you like. 
  The variable uses a file increment to name each file differently. It will concatenate the first string, the 
  increment number and '.xml'.

3. The 'if' statement in my file looks for any lines in the CSV that start with 'uribase'. This is because my files all 
  start with this and I didn't want to include it in my sitemaps. You can choose to either remove the if/else statement 
  altogether or change 'uribase' to something you'd like to ignore.
  
4. At this time the script is set up to be run using IDLE, so just open it and run it or call it via command line. 
  Feel free to fork this and make it a daemon on Linux or a Windows service if you like.

That's it. I don't think I'll be making changes to this, but who knows. Feel free to fork away and use this work or 
enhance it.

Zach zrdunlap@gmail.com
