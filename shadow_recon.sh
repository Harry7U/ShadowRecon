#!/bin/bash

# Function to display usage instructions
usage() {
  echo "Usage: $0 --target <target> [--threads <threads>] [--scan <scans>] [--output <output_dir>] [--verbose]"
  exit 1
}

# Default values
THREADS=50
SCANS="all"
OUTPUT_DIR="./results"
VERBOSE=false

# Parse command line arguments
while [ "$1" != "" ]; do
  case $1 in
    --target ) shift
               TARGET=$1
               ;;
    --threads ) shift
                THREADS=$1
                ;;
    --scan ) shift
             SCANS=$1
             ;;
    --output ) shift
               OUTPUT_DIR=$1
               ;;
    --verbose ) VERBOSE=true
                ;;
    * ) usage
        ;;
  esac
  shift
done

# Check if target is provided
if [ -z "$TARGET" ]; then
  usage
fi

# Create output directory if not exists
mkdir -p $OUTPUT_DIR
mkdir -p ./logs

# Run the setup module
echo "[*] Setting up environment..."
python3 modules/auto_setup.py --target $TARGET --threads $THREADS --output $OUTPUT_DIR --verbose $VERBOSE

# Run the recon module
echo "[*] Running subdomain enumeration..."
python3 modules/recon.py --target $TARGET --output $OUTPUT_DIR --verbose $VERBOSE

# Run the live scan module
echo "[*] Detecting live hosts..."
python3 modules/live_scan.py --output $OUTPUT_DIR --verbose $VERBOSE

# Run the URL extraction module
echo "[*] Extracting URLs and JavaScript files..."
python3 modules/url_extract.py --output $OUTPUT_DIR --verbose $VERBOSE

# Run the sensitive discovery module
echo "[*] Discovering sensitive files..."
python3 modules/sensitive_discovery.py --output $OUTPUT_DIR --verbose $VERBOSE

# Run the vulnerability scanner module
echo "[*] Scanning for vulnerabilities..."
python3 modules/vuln_scanner.py --output $OUTPUT_DIR --verbose $VERBOSE

# Run the exploitation module
if [[ "$SCANS" == *"exploit"* ]] || [[ "$SCANS" == "all" ]]; then
  echo "[*] Running exploitation tests..."
  python3 modules/exploitation.py --output $OUTPUT_DIR --verbose $VERBOSE
fi

# Run the reporting module
echo "[*] Generating reports..."
python3 modules/reporting.py --output $OUTPUT_DIR --verbose $VERBOSE

echo "[*] Scan completed. Results saved in $OUTPUT_DIR"
