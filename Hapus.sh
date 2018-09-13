!/bin/bash

server="10.0.1.100"
user="osboxes"


sshpass -p 'osboxes.org' ssh -t -o StrictHostKeyChecking=no $user@$server sudo "python Desktop/SRPLG_RULE/flush.py"
