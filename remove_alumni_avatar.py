from glob import glob
import re
import os

authors = glob('content/authors/*')
for aut in authors:
    with open(aut+'/_index.md', 'r') as f:
        lines = f.read()

    if len(re.findall(r'user_groups:\s*\n(?:\s*-\s*.*Alumni.*\n?)+', lines))>0:
        try:
            try:
                os.rename(aut+'/avatar.png', aut+'/alumni_avatar.png')
            except:
                try:
                    os.rename(aut+'/avatar.jpg', aut+'/alumni_avatar.jpg')
                except:
                    os.rename(aut+'/avatar.jpeg', aut+'/alumni_avatar.jpeg')
        except:
            continue

        print("Avatar renamed for ", aut)