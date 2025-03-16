# YNAB CSV Prepare

A script to transform a Mein Elba transaction record csv in order to be loadable by ynab.

The cvs downloaded from elba has no headers and no field with a compatible date format for the ynab converter. This scripts automates the manual tasks of adding the field and adding the headers.

## Usage

./ynab-csv-prepare.py <path/to/csv>

## Author

fgierlinger

## License

See [LICENSE](./LICENSE)
