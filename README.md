# 🌟 ShadowRecon 🌟

Welcome to **ShadowRecon**, your ultimate automated bug hunting and security reconnaissance tool. This tool is designed to streamline the process of finding vulnerabilities and gathering intelligence on your target.

## 🚀 Features

- **Automated Setup**: Installs all necessary dependencies and tools automatically.
- **Comprehensive Reconnaissance**: Enumerates subdomains, finds live hosts, and extracts URLs and JavaScript files.
- **Vulnerability Scanning**: Scans for known vulnerabilities using various tools.
- **Exploitation**: Detects potential exploits and runs automated tests.
- **Reporting**: Generates detailed reports in JSON, CSV, Markdown, and HTML formats.

## 🛠️ Installation

To get started with ShadowRecon, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Harry7U/ShadowRecon.git
cd ShadowRecon
pip install -r requirements.txt
```

## 🔍 Usage

Run the tool by specifying the target domain or IP address:

```bash
python3 main.py --target example.com
```

### Available Modules

- `setup`: Install dependencies
- `recon`: Enumerate subdomains
- `livescan`: Find live hosts
- `url_extract`: Extract URLs and JavaScript files
- `vuln`: Scan for vulnerabilities
- `exploit`: Detect exploits
- `report`: Generate reports

Example of running specific modules:

```bash
python3 main.py --target example.com --modules recon livescan vuln
```

## 📊 Reporting

ShadowRecon generates structured reports in multiple formats to suit your needs:

- **JSON**: `report.json`
- **CSV**: `report.csv`
- **Markdown**: `report.md`
- **HTML**: `report.html`

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any inquiries or support, feel free to reach out:

- [![Twitter](https://img.shields.io/twitter/follow/Harry7U?style=social)](https://twitter.com/Harry7U)
- [![GitHub](https://img.shields.io/github/followers/Harry7U?style=social)](https://github.com/Harry7U)

Happy bug hunting! 🕵️‍♂️🔍
