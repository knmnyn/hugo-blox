import json 
import os 
import pandas as pd 
import argparse

'''
---
# Display name
title: Yiding Ran

# Full Name (for SEO)
first_name: Yiding
last_name: Ran

# Is this the primary user of the site?
superuser: false

# Role/position
role: FYP Student (Aug '21); UROP Student (Aug '20)

# Organizations/Affiliations
organizations:
  - name: National University of Singapore, School of Computing
    url: 'http://www.comp.nus.edu.sg'

# Short bio (displayed in user profile at end of posts)
bio: FYP and UROP student 

# Highlight the author in author lists? (true/false)
highlight_name: false

# Organizational groups that you belong to (for People widget)
#   Set this to `[]` or comment out if you are not using People widget.
user_groups:
  - Undergraduate / Intern Alumnus
#  - Researchers
---
'''

class Alumnus:
    def __init__(self, csvfp, Alumnus_type):
        self.df = pd.read_csv(csvfp)
        self.Alumnus_type = Alumnus_type
        print(self.df.head())

        self.existing_people_dir = "content/authors"
        # look for all files in the existing_people_dir
        self.existing_people_dir_subdirs = os.listdir(self.existing_people_dir)
        print(self.existing_people_dir_subdirs)

        self.existing_people_name = ['George Huang', 'Po-Wei Huang']
        self.new_people_manual = ['Haochen Zhang', 'Shenhao Jiang']
        self.protection_list = ['Abhinav Ramesh Kashyap', 'Hengchang Hu', 'Ibrahim Taha Aksu']
    
    def process_Alumnus_data(self):
        # Name,Role,Interest,Years,Institute
        # Xinxiong Chen,Postgraduate Intern,NExT Search Centre,2013,Tsinghua University
        
        # if self.Alumnus_type in ['gradintern', 'secondary', 'staff']:
        #     # Add years to role in parentheses
        #     self.df['Role'] = self.df.apply(
        #         lambda row: f"{row['Role']} ({row['Years']})" 
        #         if pd.notna(row['Role']) and pd.notna(row['Years']) 
        #         else row['Role'],
        #         axis=1
        #     )

        # for all five Alumnus types, create a webpage, specify a user_groups column in the df. 
        # Create mapping from Alumnus type to user group based on content/people/index.md
        Alumnus_type2user_group = {
            'staff': 'Staff Alumni',
            'grad': 'Graduate Alumni', 
            'undergrad': 'Undergraduate / Intern Alumni',
            'gradintern': 'Undergraduate / Intern Alumni',
            'secondary': 'Secondary School Alumni'
        }
        self.df['user_groups'] = Alumnus_type2user_group[self.Alumnus_type]

        # check if "Institute" exist in the df, if not, create a new column "Institute" and set it to "National University of Singapore, School of Computing"
        if 'Institute' not in self.df.columns:
            self.df['Institute'] = "National University of Singapore, School of Computing"
            self.df['Institute_webpage'] = "https://www.comp.nus.edu.sg"

    
    def check_if_name_exists(self, name):
        if name in self.new_people_manual:
            return 0
        name_concat = name.replace(' ', '')
        for existing_name in self.existing_people_dir_subdirs:
            if len(existing_name) <= 4:
                continue
            if existing_name in name_concat.lower():
                print(f"{name} exists, the existing name is {existing_name}")
                return existing_name
        return 0
    
    def loop_webpage_creation(self):
        output_dir = 'content/authors'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        print('looping through the dataframe')
        for index, row in self.df.iterrows():
            # get the name of the person
            name = row['Name']
            if name in self.protection_list:
                continue
            if self.Alumnus_type == 'undergrad':
                if name in [
                    'Ziheng Lin',
                    'Jin Zhao'
                ]:
                    continue
            print(index, name)
            is_existing = self.check_if_name_exists(name)
            # if is_existing != 0:
            #     continue
            sub_names = name.split(' ')
            new_alias = sub_names[0].lower() + sub_names[-1].lower()
            if self.Alumnus_type == 'grad':
                if is_existing != 0:
                    new_alias = is_existing
            print(new_alias)
            webpage_content = self.webpage_creation(row)
            # create a new dir for the new alumnus
            new_dir = os.path.join(output_dir, new_alias)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            # create a new file in the new dir
            new_file = os.path.join(new_dir, '_index.md')
            with open(new_file, 'w') as f:
                f.write(webpage_content)
            print('Written to {}'.format(new_file))


    def webpage_creation(self, row):
        role_field = row['Role']
        if self.Alumnus_type == 'grad':
            role_field = f"{role_field}. Thesis: {row['Interest']}."

        # Create webpage content based on template
        if self.Alumnus_type == 'grad':
            webpage_content = f'''---
# Display name
title: {row['Name']}

# Full Name (for SEO) 
first_name: {row['Name'].split()[0]}
last_name: {row['Name'].split()[-1]}

# Is this the primary user of the site?
superuser: false

# Role/position
role: "{role_field}"

# Organizations/Affiliations
organizations:
  - name: {row['Institute']}
    url: {row.get('Institute_webpage', '') if 'Institute_webpage' in row else ''}

# Short bio (displayed in user profile at end of posts)
bio: {row['Role']}. 

# Highlight the author in author lists? (true/false)
highlight_name: false

# Organizational groups that you belong to (for People widget)
user_groups:
  - {row['user_groups']}
---
'''

        return webpage_content
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--Alumnus_type", type=str, default="grad")
    args = parser.parse_args()

    Alumnus_types2csv_name = {
        'gradintern': 'WING Alumni Roster - Grad Intern.csv',
        'grad': 'WING Alumni Roster - Graduate.csv',
        'secondary': 'WING Alumni Roster - Secondary School Students.csv',
        'staff': 'WING Alumni Roster - Staff.csv',
        'undergrad': 'WING Alumni Roster - UG & UG Intern.csv',
    }
    
    csv_dir = "profile_alumni"
    csv_name = Alumnus_types2csv_name[args.Alumnus_type]
    csv_fp = os.path.join(csv_dir, csv_name)

    Alumnus = Alumnus(csv_fp, args.Alumnus_type)
    Alumnus.process_Alumnus_data()
    Alumnus.loop_webpage_creation()
