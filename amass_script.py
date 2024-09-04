
# Python code example used in the assignment (if required to automate steps)

import os

# Install OWASP Amass
os.system('go install -v github.com/owasp-amass/oam-tools/cmd/...@master')

# Run Amass enumeration for Utica University domain
os.system('amass enum -d utica.edu')

# Optionally, run brute-force enumeration for better discovery
os.system('amass enum -brute -d utica.edu')

# Visualize the enumeration results using oam_viz
os.system('oam_viz -d3 -d utica.edu')

# Open the generated HTML visualization
os.system('open amass.html')
