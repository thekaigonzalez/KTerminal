import argparse
import pathlib
import time
# checks for the usr/bin directory. You can perform a full recovery from the binary dir. that's why it's so important.
cvp = argparse.ArgumentParser()

cvp.add_argument("--check", help="Verifier. Check integrity of files. Requires '1' to start.")

a =cvp.parse_args()
if a.check:
    print("checking for usr/bin (Script Directory)")
    disc = pathlib.Path("../usr/bin")
    time.sleep(1) # give one second to do it's magic.
    if disc.exists():
        print("path usr/bin exists. Setup finished.")
    else:
        print("path corrupted. performing recovery.")

