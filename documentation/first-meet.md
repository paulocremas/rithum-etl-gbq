# First meeting project scopping

### Extraction

#### Questions
1. How many stores do we need to extract data from?
2. Do you know where to find the API Key? (possibly on backoffice)
3. I found on internet that there's 2 types of API for Rithum: API SOAP (legacy) and API REST (v3). Which one will we work with? Both? (You can possibly check this on backoffice)
4. Which metrics do you want to visualize?
5. Do you already know which data you wanto to extract? Should we extract all data we can from orders? This is the information we can extract from a single API call. (REST API v3)
```json
   {
     "scrollId": "string",
     "orders": [
       {
         "poNumber": "string",
         "lineItems": [
           {
             "quantity": 1,
             "dscoSupplierId": "string",
             "dscoTradingPartnerId": "string",
             "dscoItemId": "string",
             "sku": "string",
             "upc": "string",
             "ean": "string",
             "mpn": "string",
             "isbn": "string",
             "gtin": "string",
             "estimatedShipDate": "2019-08-24T14:15:22Z",
             "estimatedShipReason": "string",
             "returnsMessage": "string",
             "returnsMessageI18n": {
               "en-US": "What's up?",
               "en-CA": "What up, eh?"
             },
             "partnerSku": "string",
             "title": "string",
             "titleI18n": {
               "en-US": "What's up?",
               "en-CA": "What up, eh?"
             },
             "expectedCost": 0,
             "consumerPrice": 0,
             "personalization": "string",
             "warehouseCode": "string",
             "warehouseRetailerCode": "string",
             "warehouseDscoId": "string",
             "status": "accepted",
             "statusReason": "string",
             "cancelledQuantity": 0,
             "cancelledReason": "string",
             "cancelCode": "string",
             "acceptedQuantity": 0,
             "acceptedReason": "string",
             "rejectedQuantity": 0,
             "rejectedReason": "string",
             "lineNumber": 1000000,
             "message": "string",
             "packingInstructions": "string",
             "shipInstructions": "string",
             "receiptId": "string",
             "giftFlag": true,
             "giftReceiptId": "string",
             "giftToName": "string",
             "giftFromName": "string",
             "giftMessage": "string",
             "color": "string",
             "size": "string",
             "retailPrice": 0,
             "shippingSurcharge": 0,
             "taxes": [
               {
                 "percentage": 0,
                 "typeCode": "string",
                 "amount": 0,
                 "jurisdictionQualifier": "Customer defined",
                 "jurisdiction": "string",
                 "exemptCode": "No (Not Tax Exempt)",
                 "registrationNumber": "string",
                 "description": "string"
               }
             ],
             "amountOfSalesTaxCollected": 0,
             "taxableAmountOfSale": 0,
             "unitOfMeasure": "EA",
             "activity": [
               {
                 "action": "accept",
                 "quantity": 0,
                 "formerStatus": "accept",
                 "reason": "string",
                 "uuid": "string",
                 "activityDate": "2019-08-24T14:15:22Z",
                 "transactionId": "string",
                 "transactionDate": "2019-08-24T14:15:22Z"
               }
             ],
             "retailerItemIds": [
               "string"
             ],
             "departmentId": "string",
             "departmentName": "string",
             "merchandisingAccountId": "string",
             "merchandisingAccountName": "string",
             "bogoFlag": true,
             "bogoInstructions": "string",
             "updateDate": "2019-08-24T14:15:22Z",
             "productGroup": "string",
             "expectedDeliveryDate": "2019-08-24T14:15:22Z",
             "requiredDeliveryDate": "2019-08-24T14:15:22Z",
             "acknowledgeByDate": "2019-08-24T14:15:22Z",
             "cancelAfterDate": "2019-08-24T14:15:22Z",
             "shipByDate": "2019-08-24T14:15:22Z",
             "invoiceByDate": "2019-08-24T14:15:22Z",
             "dscoLifecycle": "string",
             "remainingQuantity": 0,
             "shippedQuantity": 0,
             "dscoTags": [
               "string"
             ],
             "consumerBalanceDue": 0,
             "consumerCreditAmountTotal": 0,
             "consumerLineNumber": 0,
             "packingSlipTitle": "string",
             "handlingAmount": 0,
             "requestedShipDate": "2019-08-24T14:15:22Z",
             "extendedExpectedCostTotal": 0,
             "retailerLineId": "string",
             "packingSlipSku": "string",
             "expectedCostAdjustmentAllowed": true,
             "supplierColor": "string",
             "supplierTitle": "string",
             "supplierSize": "string",
             "supplierProductGroup": "string",
             "weight": 0,
             "weightUnits": "string",
             "secondaryReceiptId": "string",
             "crossDockLocation": {
               "address": [
                 "string"
               ],
               "city": "string",
               "region": "string",
               "postal": "string",
               "county": "string",
               "country": "string",
               "name": "string",
               "email": "string",
               "phone": "string",
               "nightPhone": "string",
               "company": "string",
               "customerNumber": "string",
               "addressType": "commercial",
               "attention": "string",
               "locationCode": "string",
               "storeNumber": "string"
             },
             "retailerProductGroup": "string",
             "supplierQuoteNumber": "string",
             "productSpecifications": "string",
             "map": 0,
             "msrp": 0,
             "commissionPercentage": 0,
             "expectedCrossDockDeliveryDate": "2019-08-24T14:15:22Z",
             "consumerPriceWithoutTax": 0,
             "consumerPriceWithTax": 0,
             "personalizationMap": {
               "property1": "string",
               "property2": "string"
             }
           }
         ],
         "retailerCreateDate": "2019-08-24T14:15:22Z",
         "channel": "string",
         "buyer": {
           "address": [
             "string"
           ],
           "city": "string",
           "region": "string",
           "postal": "string",
           "county": "string",
           "country": "string",
           "name": "string",
           "email": "string",
           "phone": "string",
           "nightPhone": "string",
           "company": "string",
           "customerNumber": "string",
           "addressType": "commercial",
           "attention": "string",
           "locationCode": "string",
           "storeNumber": "string",
           "taxRegistrationNumber": "string",
           "buyingContractAgreementId": "string",
           "consumerCreditAmountTotal": "string"
         },
         "customer": {
           "address": [
             "string"
           ],
           "city": "string",
           "region": "string",
           "postal": "string",
           "county": "string",
           "country": "string",
           "name": "string",
           "email": "string",
           "phone": "string",
           "nightPhone": "string",
           "company": "string",
           "customerNumber": "string",
           "addressType": "commercial",
           "attention": "string",
           "locationCode": "string",
           "storeNumber": "string"
         },
         "invoiceTo": {
           "address": [
             "string"
           ],
           "city": "string",
           "region": "string",
           "postal": "string",
           "county": "string",
           "country": "string",
           "name": "string",
           "email": "string",
           "phone": "string",
           "nightPhone": "string",
           "company": "string",
           "customerNumber": "string",
           "addressType": "commercial",
           "attention": "string",
           "locationCode": "string",
           "storeNumber": "string"
         },
         "shipping": {
           "attention": "string",
           "firstName": "string",
           "lastName": "string",
           "company": "string",
           "address1": "string",
           "address2": "string",
           "city": "string",
           "region": "string",
           "state": "string",
           "postal": "string",
           "country": "string",
           "phone": "string",
           "email": "string",
           "carrier": "string",
           "method": "string",
           "storeNumber": "string",
           "name": "string",
           "address": [
             "string"
           ],
           "addressType": "Residential",
           "shipNightPhone": "string",
           "shipCustomerNumber": "string",
           "shipSiteType": "customer"
         },
         "signatureRequiredFlag": true,
         "shipInstructions": "string",
         "giftWrapFlag": true,
         "giftWrapMessage": "string",
         "supplierOrderNumber": "string",
         "dscoOrderId": "string",
         "dscoStatus": "created",
         "dscoLifecycle": "received",
         "dscoRetailerId": "string",
         "dscoSupplierId": "string",
         "dscoSupplierName": "string",
         "dscoTradingPartnerId": "string",
         "dscoTradingPartnerName": "string",
         "dscoTradingPartnerParentId": "string",
         "dscoCreateDate": "2019-08-24T14:15:22Z",
         "dscoLastUpdate": "2019-08-24T14:15:22Z",
         "testFlag": true,
         "currencyCode": "string",
         "cancelAfterDate": "2019-08-24T14:15:22Z",
         "consumerOrderNumber": "string",
         "internalControlNumber": "string",
         "orderType": "Dropship",
         "shipByDate": "2019-08-24T14:15:22Z",
         "acknowledgeByDate": "2019-08-24T14:15:22Z",
         "invoiceByDate": "2019-08-24T14:15:22Z",
         "dscoShipLateDate": "2019-08-24T14:15:22Z",
         "dscoAcknowledgeLateDate": "2019-08-24T14:15:22Z",
         "dscoCancelLateDate": "2019-08-24T14:15:22Z",
         "dscoInvoiceLateDate": "2019-08-24T14:15:22Z",
         "expectedDeliveryDate": "2019-08-24T14:15:22Z",
         "requiredDeliveryDate": "2019-08-24T14:15:22Z",
         "marketingMessage": "string",
         "message": "string",
         "packingInstructions": "string",
         "shipToStoreNumber": "string",
         "numberOfLineItems": 0,
         "giftFlag": true,
         "giftMessage": "string",
         "giftToName": "string",
         "giftFromName": "string",
         "receiptId": "string",
         "giftReceiptId": "string",
         "shippingSurcharge": 0,
         "taxes": [
           {
             "percentage": 0,
             "typeCode": "string",
             "amount": 0,
             "jurisdictionQualifier": "Customer defined",
             "jurisdiction": "string",
             "exemptCode": "No (Not Tax Exempt)",
             "registrationNumber": "string",
             "description": "string"
           }
         ],
         "amountOfSalesTaxCollected": 0,
         "taxableAmountOfSale": 0,
         "coupons": [
           {
             "amount": 0,
             "percentage": 0
           }
         ],
         "payments": [
           {
             "cardType": "string",
             "cardLastFour": "string",
             "description": "string",
             "cardTypeDetails": "string"
           }
         ],
         "billTo": {
           "attention": "string",
           "firstName": "string",
           "lastName": "string",
           "company": "string",
           "address1": "string",
           "address2": "string",
           "city": "string",
           "region": "string",
           "postal": "string",
           "country": "string",
           "phone": "string",
           "email": "string",
           "name": "string",
           "address": [
             "string"
           ],
           "addressType": "Residential"
         },
         "shipCarrier": "string",
         "shipMethod": "string",
         "shippingServiceLevelCode": "string",
         "requestedShipCarrier": "string",
         "requestedShipMethod": "string",
         "requestedShippingServiceLevelCode": "string",
         "requestedShippingServiceLevelCodeUnmapped": "string",
         "dscoShipCarrier": "string",
         "dscoShipMethod": "string",
         "dscoShippingServiceLevelCode": "string",
         "packages": [
           {
             "trackingNumber": "string",
             "untracked": true,
             "shipCost": 0,
             "shipDate": "2019-08-24T14:15:22Z",
             "shipCarrier": "string",
             "shipMethod": "string",
             "items": [
               {
                 "titleI18n": {
                   "en-US": "What's up?",
                   "en-CA": "What up, eh?"
                 },
                 "quantity": 0,
                 "dscoItemId": "string",
                 "sku": "string",
                 "partnerSku": "string",
                 "upc": "string",
                 "ean": "string",
                 "lineNumber": 0,
                 "originalLineNumber": 0,
                 "originalOrderQuantity": 0,
                 "retailerItemIds": [
                   "string"
                 ],
                 "retailerLineId": "string",
                 "departmentId": "string",
                 "departmentName": "string",
                 "merchandisingAccountId": "string",
                 "merchandisingAccountName": "string",
                 "serialNumbers": [
                   "string"
                 ],
                 "packageSpanFlag": true
               }
             ],
             "currencyCode": "string",
             "shippingServiceLevelCode": "string",
             "dscoActualShipMethod": "string",
             "dscoActualShipCarrier": "string",
             "dscoActualShippingServiceLevelCode": "string",
             "dscoActualShipCost": 0,
             "dscoActualDeliveryDate": "2019-08-24T14:15:22Z",
             "dscoActualPickupDate": "2019-08-24T14:15:22Z",
             "returnedFlag": true,
             "returnDate": "2019-08-24T14:15:22Z",
             "returnNumber": "string",
             "returnReason": "string",
             "numberOfLineItems": 0,
             "packageShipFrom": {
               "attention": "string",
               "firstName": "string",
               "lastName": "string",
               "company": "string",
               "address1": "string",
               "address2": "string",
               "city": "string",
               "region": "string",
               "postal": "string",
               "country": "string",
               "phone": "string",
               "email": "string",
               "taxExemptNumber": "string",
               "taxRegistrationNumber": "string",
               "locationCode": "string",
               "name": "string",
               "address": [
                 "string"
               ],
               "addressType": "Residential"
             },
             "packageShipTo": {
               "attention": "string",
               "firstName": "string",
               "lastName": "string",
               "company": "string",
               "address1": "string",
               "address2": "string",
               "city": "string",
               "region": "string",
               "postal": "string",
               "country": "string",
               "phone": "string",
               "email": "string",
               "storeNumber": "string",
               "taxExemptNumber": "string",
               "taxRegistrationNumber": "string",
               "name": "string",
               "address": [
                 "string"
               ],
               "addressType": "Residential"
             },
             "dscoPackageId": 0,
             "shipWeight": 0,
             "shipWeightUnits": "string",
             "warehouseCode": "string",
             "warehouseRetailerCode": "string",
             "warehouseDscoId": "string",
             "ssccBarcode": "string",
             "referenceNumberQualifier": "2I",
             "transportationMethodCode": "A",
             "unitOfMeasurementCode": "CA",
             "carrierManifestId": "string",
             "dscoTradingPartnerParentId": "string",
             "transactionId": "string",
             "transactionDate": "2019-08-24T14:15:22Z",
             "vendorInvoiceNumber": "string",
             "balanceDue": 0
           }
         ],
         "requestedWarehouseCode": "string",
         "requestedWarehouseRetailerCode": "string",
         "requestedWarehouseDscoId": "string",
         "dscoWarehouseCode": "string",
         "dscoWarehouseRetailerCode": "string",
         "dscoWarehouseDscoId": "string",
         "shipWarehouseCode": "string",
         "shipWarehouseRetailerCode": "string",
         "shipWarehouseDscoId": "string",
         "packingSlipMessage": "string",
         "retailerAccountsPayableId": "string",
         "authorizationForExpenseNumber": "string",
         "customerMembershipId": "string",
         "releaseNumber": "string",
         "orderTotalAmount": 0,
         "shippingAccountNumber": "string",
         "returnsMessage": "string",
         "returnsMessageI18n": {
           "en-US": "What's up?",
           "en-CA": "What up, eh?"
         },
         "customerBalanceDue": 0,
         "secondaryConsumerOrderNumber": "string",
         "issuerDivision": "string",
         "consumerOrderDate": "2019-08-24T14:15:22Z",
         "extendedExpectedCostTotal": 0,
         "packingSlipEmail": "string",
         "packingSlipPhone": "string",
         "packingSlipTemplate": "string",
         "consumerOrderCurrencyCode": "string",
         "secondaryReceiptId": "string",
         "primaryBatchNumber": "string",
         "secondaryBatchNumber": "string",
         "businessRuleCode": "string",
         "salesRevenueCenter": "string",
         "salesAgent": "string",
         "departmentId": "string",
         "departmentName": "string",
         "expectedCrossDockDeliveryDate": "2019-08-24T14:15:22Z",
         "crossDockFlag": true,
         "crossDockLocation": {
           "address": [
             "string"
           ],
           "city": "string",
           "region": "string",
           "postal": "string",
           "county": "string",
           "country": "string",
           "name": "string",
           "email": "string",
           "phone": "string",
           "nightPhone": "string",
           "company": "string",
           "customerNumber": "string",
           "addressType": "commercial",
           "attention": "string",
           "locationCode": "string",
           "storeNumber": "string"
         },
         "deliveryMethod": "in_store_pickup"
       }
     ]
   }
   ```
   
#### Requirements
3.
4. For API REST (v3) I need at least 1 access token. Preferably of a read only account.
5. 

### Load

### Dashboad
