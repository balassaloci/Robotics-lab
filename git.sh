git add --all;
echo "ADDED";
echo -n "Enter Commit Name > ";
read text;
git commit -a -m \"$text\";
git push;