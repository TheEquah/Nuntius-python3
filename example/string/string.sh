# Author (Created): Roger "Equah" Hürzeler
# Date (Created): 12020.03.22 HE
# License: apache-2.0


SRC_DIR="`dirname $0`/../../src"
MAIN_DIR="`dirname $0`"

echo "=== INSTALL ==="
cd $SRC_DIR
sudo python3 ./setup.py install

echo "=== EXECUTE ==="
cd ../$MAIN_DIR
python3 ./string.py

echo "=== END ==="
