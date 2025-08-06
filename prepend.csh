#csh to prepend standard input to file argument
#Version 2
if($#argv!=1) then    #Check for number of arguments
    echo "Usage: ppd output_file"
    exit 1 #exit on error
endif
set tf = /tmp/ppd.$$ #Name temp file
set dest = $argv[1]. #Get argument name
if(-w$dest) then          #Make sure it's writable
    cat - $dest > $tf #Concatenate $tf with target
    mv $tf $dest #Replace original file
    exit 0 #Exit with good status
endif

if(-e$dest) then #Does it exist?
    echo "ppd:$dest not writable."
else
    echo "ppd:$dest does not exist."
endif
exit 1 #Exit on error
    
