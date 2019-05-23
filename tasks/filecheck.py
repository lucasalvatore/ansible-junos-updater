import filecmp
import os


# Determine the items that exist in both directories
pre_checks = set(os.listdir('pre-checks/'))
post_checks = set(os.listdir('post-checks/'))
common = list(pre_checks & post_checks)
common_files = [
    f
    for f in common
    if os.path.isfile(os.path.join('post-checks/', f))
]

# Compare the directories
match, mismatch, errors = filecmp.cmpfiles('pre-checks/', 'post-checks/', common_files)

#print("No Changes detected in:", *match, sep = "\n")
print("#" * 40)
print("Changes detected in:", *mismatch, sep = "\n")
print("#" * 40)
print('Error Reading:', *errors, sep = "\n")
