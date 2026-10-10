function mvlast() {
     mv "/mnt/c/Users/kathe/Downloads/$(ls -rt \
          /mnt/c/Users/kathe/Downloads | tail -n 1)" $1 
}

function mvlast() {
     for ((i=1; i<=${i}; i++)); do
     mv "/mnt/c/Users/kathe/Downloads/$(ls -rt \
          /mnt/c/Users/kathe/Downloads | tail -n 1)" $1 
     done
}

nJobs=30
for (( i=1; i<=${nJobs}; i++ )); do
   python job.py > job-${i}.out &
done