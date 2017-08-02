# This bash script works in Linux and macOS, assuming the python executable is
# in the path. It creates a symbolic link to the scoria directory from this
# one.

# A very similar command should work in Windows. Just copy the scoria directory to
# this one before running.

# Make the symbolic link (Linux and macOS).
ln -s ../scoria ./

# Run footprint.py using the python executable, which should be in the path.
python footprint.py