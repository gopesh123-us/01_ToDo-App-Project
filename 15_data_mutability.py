filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"];
new_filenames = [];
for index, filename in enumerate(filenames):
    filename = filename.replace(".", "_", 1);
    new_filenames.append(filename);

print(new_filenames);

usernames = ['the blueman', 'sorted hedgehog', 'infinite lagoon']

for user in usernames:
    user = user.replace(" ", "_")
    print(user)