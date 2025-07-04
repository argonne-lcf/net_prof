# Changelog:
## [0.1.6] - 7-3-2025
### Added
- normalizing name as net_prof (instead of juggling net-prof for pip and net_prof for python)

## [0.1.5] - 7-3-2025
### Added
- Fixed missing required .txt and .csv files from pypi package (net-prof/src/net_prof/data/metrics.txt & grouping_rules.csv) (added via .toml)
- Updated README - Fixes to examples, added Aurora test run to examples.
- Updated Description in .toml
- Removed engine (copy).py -- Removed other unneccesary files
- Added statements that print out relating to image generation including dir of images
- Added timestamp to html output.


## [0.1.4] - 7-2-2025
### Added
- Fixed naming conventions within grouping_rules.csv, which was causing counters with numbers to not be tracked into the right group.
- New bug detected: If a counter belongs to more than one group, it only casts to the first group, and doesn't track the counter within the second group.

## [0.1.3] - 6-26-2025
### Added
- Added timestamp_ISO_8601 to JSON file for human readable time.
- Added new validation for collect(), adding these error messages:
    - Path {input_path!r} is neither a telemetry directory nor a parent of cxi* interfaces.
    - No valid cxi*/device/telemetry subfolders found under {input_path!r}
    - Warning: {telemetry_dir!r} is empty, skipping. 
    - Telemetry directory {input_path!r} contains no files.
    - Path {input_path!r} does not exist or is not a directory.

## [0.1.2] - 06-26-2025
### Added
- Multi-interface profiling
    - Retrofitted old collect() into helper function _collect_one_interface().
    - Changes to collect() to allow multi-interface, while using _collect_one_interface() for single interface profiling.
- introduced new test, test_iface_all.py

### Fixed
- Typo in __init__.py -- '.' in place of ','
- Typo in README.md -- 'import net-prof' to 'import net_prof'

## [0.1.1] - 06-25-2025
### Added
- CHANGELOG.md

### Fixed
- Got rid of Changelog from README.md.
- Forgot to update README.md before uploading to PYpi
- Didn't tag to github first for 0.1.0 so doing that now



## [0.1.0] - 06-25-2025
- Initial PyPI release
### Added
- Uploaded to pypi: https://pypi.org/project/net-prof/0.1.0/
- Changes to README.md

### Fixed
- Removed requirements.txt -- replaced with [dependencies] in .toml
- Added [dependencies] to pyproject.toml -- will be auto-installed with 'pip install net-prof'

