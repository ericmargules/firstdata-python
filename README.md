# FirstData Global Payment API Python library

## Dependencies

* Python 2.6, 2.7, 3.3, 3.4, or 3.5

## Quick Start Example

    import firstdata

    fd = firstdata.Portal({
      'api_key': 'Enter Api Key here',
      'api_secret': 'Enter Api Secret here',
      'app_id': 'Enter App ID here'
    })

    sale = fd.transaction.sale({
        'amount': {
          'total': '100.00',
          'currency': 'USD'
        },
        'payment_method': {
          'type': 'PAYMENT_CARD',
          'payment_card': {
            'number': '4111111111111111',
            'expiry_date': '1223'
          }
        }
    })

    if sale.is_successful:
        print('Transaction' + sale.ipgTransactionId + ' was successful!')
    else:
        print('Error processing transaction:\n')
        print('Message: ' + sale.error.message)

## License

See the [LICENSE](LICENSE) file for more info.