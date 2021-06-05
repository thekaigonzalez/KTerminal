parameterA=$1
parameterB=$2
parameterC=$3
if [ -z "$parameterC" ]
then
gcc "$parameterA" -fPIC -shared -o "$parameterB"
else
    gcc "$parameterA" -fPIC -shared -o "$parameterB" "$parameterC"

fi
