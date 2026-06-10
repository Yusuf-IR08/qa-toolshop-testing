test_data = [
    (
        "TC_LOGIN_001",
        "customer2@practicesoftwaretesting.com",
        "welcome01",
        True
    ),
    (
        "TC_LOGIN_002",
        "wrongcustomer@practicesoftwaretesting.com",
        "welcome01",
        False
    ),
    (
        "TC_LOGIN_003",
        "customer2@practicesoftwaretesting.com",
        "wrongpassword",
        False
    ),
    (
        "TC_LOGIN_004",
        "",
        "",
        False
    ),
    (
        "TC_LOGIN_005",
        "",
        "welcome01",
        False
    ),
    (
        "TC_LOGIN_006",
        "customer2@practicesoftwaretesting.com",
        "",
        False
    ),
    # (
    #     "TC_LOGIN_007",
    #     login menggunakan akun google yang eregistrasi
    # ),
    # (
    #     "TC_LOGIN_008",
    #     login menggunakan akun google yang belum teregistrasi
    # ),
    (
        "TC_LOGIN_009",
        "customer@practice@softwaretesting.com",
        "welcome01",
        False
    ),
    # (
    #     "TC_LOGIN_010",
    #     klik register untuk daftar akun
    # ),
    # (
    #     "TC_LOGIN_011",
    #     klik forgot password untuk mengatur password baru
    # ),
    # (
    #     "TC_LOGIN_012",
    #     logout dari akun yang sudah terdaftar
    # ),
    (
        "TC_LOGIN_013",
        "customer@practicesoftwaretesting.com",
        "wrongpassword",
        "locked"
    )
]