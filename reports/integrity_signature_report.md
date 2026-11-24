# Целостность и подпись

Учебная модель, не для реальной защиты.
Не является юридически значимой УКЭП.
TLS-модель не совместима с реальным протоколом.

[
  {
    "algorithm": "sha256",
    "operation": "digest",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "1df2a677a75b2d7903b7bf838e2a2137e8e783fdf551a4a86f800b3dc33f5cf0",
    "key_or_params": {},
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "sha256",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "1df2a677a75b2d7903b7bf838e2a2137e8e783fdf551a4a86f800b3dc33f5cf0",
    "key_or_params": {},
    "status": "ok",
    "explanation": "Хеш совпал."
  },
  {
    "algorithm": "sha256",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.!",
    "result": "50c62e968b14e5d9fbe059f3b912c5c5cb43051841e8a0d364ccf58df4039973",
    "key_or_params": {},
    "status": "error",
    "explanation": "Хеш изменился."
  },
  {
    "algorithm": "aes_gcm",
    "operation": "encrypt",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "1513e8e30348b3e7d8dcd51a94caea8a7bb952b6b6f0b85052a3f221162a404d4a908ffeb6fbf6271fb361b151d91beed6ead5968f8174be33536510b94cb2e1fae5cea0e4760dd9ca58aa6a367832a316727893e1ad36e63ca10ef09b0e05b5600cfc2f23f36c9d540c9bca46501dde15565338f2937f28784f12",
    "key_or_params": {
      "nonce": "1513e8e30348b3e7d8dcd51a",
      "tag_bytes": 16
    },
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "aes_gcm",
    "operation": "decrypt",
    "source_message": "1513e8e30348b3e7d8dcd51a94caea8a7bb952b6b6f0b85052a3f221162a404d4a908ffeb6fbf6271fb361b151d91beed6ead5968f8174be33536510b94cb2e1fae5cea0e4760dd9ca58aa6a367832a316727893e1ad36e63ca10ef09b0e05b5600cfc2f23f36c9d540c9bca46501dde15565338f2937f28784f12",
    "result": "Учебная записка. Макет лабораторного стенда принят.",
    "key_or_params": {},
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "aes_gcm",
    "operation": "decrypt",
    "source_message": "1513e8e30348b3e7d8dcd51a94caea8a7bb952b6b6f0b85052a3f221162a404d4a908ffeb6fbf6271fb361b151d91beed6ead5968f8174be33536510b94cb2e1fae5cea0e4760dd9ca58aa6a367832a316727893e1ad36e63ca10ef09b0e05b5600cfc2f23f36c9d540c9bca46501dde15565338f2937f28784f13",
    "result": "",
    "key_or_params": {},
    "status": "error",
    "explanation": "Проверка аутентичности AES-GCM не пройдена."
  }
]

[
  {
    "algorithm": "ecdsa",
    "operation": "sign",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "{\"digest\": \"1df2a677a75b2d7903b7bf838e2a2137e8e783fdf551a4a86f800b3dc33f5cf0\", \"der\": \"304402203ea073a489b1352acd786ce9a56bb7201e459972f986df94e4018ca6f3280e3e02206856c14280b88e2d36ba860fb31d3f8194d0a75bae28aa7e94801da30354682b\"}",
    "key_or_params": {},
    "status": "ok",
    "explanation": ""
  },
  {
    "algorithm": "ecdsa",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "действительна",
    "key_or_params": {},
    "status": "ok",
    "explanation": "действительна"
  },
  {
    "algorithm": "ecdsa",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.!",
    "result": "документ изменён",
    "key_or_params": {},
    "status": "error",
    "explanation": "документ изменён"
  },
  {
    "algorithm": "ecdsa",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "недействительна",
    "key_or_params": {},
    "status": "error",
    "explanation": "недействительна"
  },
  {
    "algorithm": "ecdsa",
    "operation": "verify",
    "source_message": "Учебная записка. Макет лабораторного стенда принят.",
    "result": "недействительна",
    "key_or_params": {},
    "status": "error",
    "explanation": "недействительна"
  },
  {
    "algorithm": "certificate",
    "operation": "inspect",
    "source_message": "relay.example.test",
    "result": "{\"subject\": \"relay.example.test\", \"issuer\": \"CryptoLab Demo CA\", \"valid_from\": \"2026-01-01\", \"valid_until\": \"2027-01-01\", \"serial\": \"DEMO-005\", \"status\": \"active\", \"purpose\": \"server\"}",
    "key_or_params": {},
    "status": "ok",
    "explanation": "Условная проверка карточки пройдена."
  }
]

### Виды электронной подписи

| Вид | Механизм | Ключи | Сертификат | Проверка | Признание |
| --- | --- | --- | --- | --- | --- |
| ПЭП | Коды, пароли или иные средства подтверждения | не требуется по определению | не требуется | определение подписанта по правилам системы | в случаях, установленных применимыми актами или соглашением |
| УНЭП | Криптографическое преобразование | ключ подписи и ключ проверки | квалифицированный сертификат не обязателен | определение подписанта и обнаружение изменений | в случаях, установленных применимыми актами или соглашением |
| УКЭП | Усиленная подпись с дополнительными требованиями | ключ проверки указан в квалифицированном сертификате | квалифицированный | подпись, сертификат и применимые ограничения | общий режим равнозначности собственноручной подписи с предусмотренными законом исключениями |
