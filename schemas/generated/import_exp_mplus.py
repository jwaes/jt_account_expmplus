from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


class AccountCategoryTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class AccountTypeTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_22 = 22
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56


@dataclass
class AnalyticType:
    analytic: List["AnalyticType.Analytic"] = field(
        default_factory=list,
        metadata={
            "name": "Analytic",
            "type": "Element",
        }
    )

    @dataclass
    class Analytic:
        level1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Level1",
                "type": "Element",
            }
        )
        level2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Level2",
                "type": "Element",
            }
        )
        level3: Optional[str] = field(
            default=None,
            metadata={
                "name": "Level3",
                "type": "Element",
            }
        )
        level4: Optional[str] = field(
            default=None,
            metadata={
                "name": "Level4",
                "type": "Element",
            }
        )
        level5: Optional[str] = field(
            default=None,
            metadata={
                "name": "Level5",
                "type": "Element",
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        unit1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit1",
                "type": "Element",
            }
        )
        unit2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit2",
                "type": "Element",
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "Ref",
                "type": "Element",
                "max_length": 255,
            }
        )


class BoolTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


class DatePayedType(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class DebCreType(Enum):
    VALUE_1 = 1
    VALUE_1_1 = -1


class DelivDateType(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class DocStateType(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class DocTypeType(Enum):
    VALUE_10 = 10
    VALUE_30 = 30


class DueTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class FinDocTypeType(Enum):
    VALUE_20 = 20
    VALUE_40 = 40
    VALUE_120 = 120
    VALUE_140 = 140
    VALUE_999 = 999


class FinVentilType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class IntrastatDeliveryType(Enum):
    EXW = "EXW"
    FCA = "FCA"
    FAS = "FAS"
    FOB = "FOB"
    CFR = "CFR"
    CIF = "CIF"
    CPT = "CPT"
    CIP = "CIP"
    DAF = "DAF"
    DES = "DES"
    DEQ = "DEQ"
    DDU = "DDU"
    DDP = "DDP"
    XXX = "XXX"
    VALUE_0 = "0"


class IntrastatTransportType(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"


class LanguageTypeValue(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class LevelType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class ModuleType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


class RegionType(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StateTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class StatusType(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class SunVentilType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class TransferTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class TransportType(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class TypeAanTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class TypeDivTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_61 = 61
    VALUE_62 = 62
    VALUE_70 = 70
    VALUE_71 = 71


class TypeFinTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13


class UnitDecTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class VatcodeTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class VatstatusTypeValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


@dataclass
class AccountType:
    account: List["AccountType.Account"] = field(
        default_factory=list,
        metadata={
            "name": "Account",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Account:
        prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Prime",
                "type": "Element",
                "required": True,
            }
        )
        alt_key: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "AltKey",
                "type": "Element",
                "length": 0,
            }
        )
        description1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description1",
                "type": "Element",
                "max_length": 255,
            }
        )
        description2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description2",
                "type": "Element",
                "max_length": 255,
            }
        )
        description3: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description3",
                "type": "Element",
                "max_length": 255,
            }
        )
        description4: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description4",
                "type": "Element",
                "max_length": 255,
            }
        )
        type: Optional[Union[str, AccountCategoryTypeValue]] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Element",
                "length": 0,
            }
        )
        private_exp: Optional[str] = field(
            default=None,
            metadata={
                "name": "PrivateExp",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        vatnd: Optional[str] = field(
            default=None,
            metadata={
                "name": "VATND",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        rejected_exp: Optional[str] = field(
            default=None,
            metadata={
                "name": "RejectedExp",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        book_purchases: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "BookPurchases",
                "type": "Element",
                "length": 0,
            }
        )
        book_sales: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "BookSales",
                "type": "Element",
                "length": 0,
            }
        )
        book_financial: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "BookFinancial",
                "type": "Element",
                "length": 0,
            }
        )
        book_sundries: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "BookSundries",
                "type": "Element",
                "length": 0,
            }
        )
        detail: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Detail",
                "type": "Element",
                "length": 0,
            }
        )
        transfer: Optional[Union[str, TransferTypeValue]] = field(
            default=None,
            metadata={
                "name": "Transfer",
                "type": "Element",
                "length": 0,
            }
        )
        account_type: Optional[Union[str, AccountTypeTypeValue]] = field(
            default=None,
            metadata={
                "name": "AccountType",
                "type": "Element",
                "length": 0,
            }
        )
        free_field1: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField1",
                "type": "Element",
                "max_length": 255,
            }
        )
        free_field2: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField2",
                "type": "Element",
                "max_length": 255,
            }
        )
        free_field3: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField3",
                "type": "Element",
                "max_length": 255,
            }
        )
        free_field4: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField4",
                "type": "Element",
                "max_length": 255,
            }
        )
        unit1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit1",
                "type": "Element",
                "max_length": 5,
            }
        )
        unit2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit2",
                "type": "Element",
                "max_length": 5,
            }
        )
        unit1_dec: Optional[Union[str, UnitDecTypeValue]] = field(
            default=None,
            metadata={
                "name": "Unit1Dec",
                "type": "Element",
                "length": 0,
            }
        )
        unit2_dec: Optional[Union[str, UnitDecTypeValue]] = field(
            default=None,
            metadata={
                "name": "Unit2Dec",
                "type": "Element",
                "length": 0,
            }
        )
        per_cars: Optional[Union[str, TransferTypeValue]] = field(
            default=None,
            metadata={
                "name": "PerCars",
                "type": "Element",
                "length": 0,
            }
        )
        double_turnover: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "DoubleTurnover",
                "type": "Element",
                "length": 0,
            }
        )
        crea_doc: Optional[Union[str, TransferTypeValue]] = field(
            default=None,
            metadata={
                "name": "CreaDoc",
                "type": "Element",
                "length": 0,
            }
        )
        account_act_pas: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Account_ActPas",
                "type": "Element",
                "length": 0,
            }
        )
        account_vatnd: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Account_VATND",
                "type": "Element",
                "length": 0,
            }
        )
        anal1: Optional[Union[str, TransferTypeValue]] = field(
            default=None,
            metadata={
                "name": "Anal1",
                "type": "Element",
                "length": 0,
            }
        )
        anal2: Optional[Union[str, TransferTypeValue]] = field(
            default=None,
            metadata={
                "name": "Anal2",
                "type": "Element",
                "length": 0,
            }
        )
        invest: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Invest",
                "type": "Element",
                "length": 0,
            }
        )
        account_depr: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Account_Depr",
                "type": "Element",
                "length": 0,
            }
        )
        invest_allowance: Optional[Union[str, TransferTypeValue]] = field(
            default=None,
            metadata={
                "name": "InvestAllowance",
                "type": "Element",
                "length": 0,
            }
        )
        method_depr: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "MethodDepr",
                "type": "Element",
                "length": 0,
            }
        )
        term_depr: Optional[str] = field(
            default=None,
            metadata={
                "name": "TermDepr",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        term_depr_yr: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "TermDeprYr",
                "type": "Element",
                "length": 0,
            }
        )
        coef_res_val: Optional[str] = field(
            default=None,
            metadata={
                "name": "CoefResVal",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        state: Optional[Union[str, StateTypeValue]] = field(
            default=None,
            metadata={
                "name": "State",
                "type": "Element",
                "length": 0,
            }
        )
        status: Optional[StatusType] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class AnalyticAccountType:
    analytic_account: List["AnalyticAccountType.AnalyticAccount"] = field(
        default_factory=list,
        metadata={
            "name": "AnalyticAccount",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class AnalyticAccount:
        module: Optional[ModuleType] = field(
            default=None,
            metadata={
                "name": "Module",
                "type": "Element",
                "required": True,
            }
        )
        level: Optional[LevelType] = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Element",
                "required": True,
            }
        )
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Element",
                "required": True,
            }
        )
        description1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description1",
                "type": "Element",
                "max_length": 255,
            }
        )
        description2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description2",
                "type": "Element",
                "max_length": 255,
            }
        )
        description3: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description3",
                "type": "Element",
                "max_length": 255,
            }
        )
        description4: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description4",
                "type": "Element",
                "max_length": 255,
            }
        )
        allocation_key: Optional[str] = field(
            default=None,
            metadata={
                "name": "AllocationKey",
                "type": "Element",
            }
        )
        closed: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Closed",
                "type": "Element",
                "length": 0,
            }
        )
        free_field1: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField1",
                "type": "Element",
            }
        )
        free_field2: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField2",
                "type": "Element",
            }
        )
        free_field3: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField3",
                "type": "Element",
            }
        )
        free_field4: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField4",
                "type": "Element",
            }
        )
        status: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )


@dataclass
class CustomerType:
    customer: List["CustomerType.Customer"] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Customer:
        prime: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Prime",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        alfa: Optional[str] = field(
            default=None,
            metadata={
                "name": "Alfa",
                "type": "Element",
                "max_length": 10,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
                "max_length": 255,
            }
        )
        country: Optional[str] = field(
            default=None,
            metadata={
                "name": "Country",
                "type": "Element",
                "required": True,
                "max_length": 2,
            }
        )
        street: Optional[str] = field(
            default=None,
            metadata={
                "name": "Street",
                "type": "Element",
                "max_length": 60,
            }
        )
        house_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "HouseNumber",
                "type": "Element",
                "max_length": 10,
            }
        )
        mailbox_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "MailboxNumber",
                "type": "Element",
                "max_length": 5,
            }
        )
        zip_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ZipCode",
                "type": "Element",
                "max_length": 10,
            }
        )
        city: Optional[str] = field(
            default=None,
            metadata={
                "name": "City",
                "type": "Element",
                "max_length": 50,
            }
        )
        language: Optional[Union[str, LanguageTypeValue]] = field(
            default=None,
            metadata={
                "name": "Language",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Element",
                "required": True,
                "max_length": 3,
            }
        )
        vatcode: Optional[Union[str, VatcodeTypeValue]] = field(
            default=None,
            metadata={
                "name": "VATCode",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        vatstatus: Optional[Union[str, VatstatusTypeValue]] = field(
            default=None,
            metadata={
                "name": "VATStatus",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        country_vatnumber: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryVATNumber",
                "type": "Element",
                "max_length": 2,
            }
        )
        vatnumber: Optional[str] = field(
            default=None,
            metadata={
                "name": "VATNumber",
                "type": "Element",
                "max_length": 30,
            }
        )
        rappel: Optional[Union[str, VatcodeTypeValue]] = field(
            default=None,
            metadata={
                "name": "Rappel",
                "type": "Element",
                "length": 0,
            }
        )
        dom: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Dom",
                "type": "Element",
                "length": 0,
            }
        )
        extra1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Extra1",
                "type": "Element",
                "max_length": 255,
            }
        )
        extra2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Extra2",
                "type": "Element",
                "max_length": 255,
            }
        )
        extra3: Optional[str] = field(
            default=None,
            metadata={
                "name": "Extra3",
                "type": "Element",
                "max_length": 255,
            }
        )
        phone: Optional[str] = field(
            default=None,
            metadata={
                "name": "Phone",
                "type": "Element",
                "max_length": 30,
            }
        )
        fax: Optional[str] = field(
            default=None,
            metadata={
                "name": "Fax",
                "type": "Element",
                "max_length": 30,
            }
        )
        gsm: Optional[str] = field(
            default=None,
            metadata={
                "name": "GSM",
                "type": "Element",
                "max_length": 30,
            }
        )
        email: Optional[str] = field(
            default=None,
            metadata={
                "name": "Email",
                "type": "Element",
                "max_length": 50,
            }
        )
        account_sale: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "AccountSale",
                "type": "Element",
                "length": 0,
            }
        )
        goods_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "GoodsCode",
                "type": "Element",
                "max_length": 8,
            }
        )
        intrastat_transport: Optional[IntrastatTransportType] = field(
            default=None,
            metadata={
                "name": "IntrastatTransport",
                "type": "Element",
            }
        )
        intrastat_transaction: Optional[IntrastatTransportType] = field(
            default=None,
            metadata={
                "name": "IntrastatTransaction",
                "type": "Element",
            }
        )
        country_bank_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber",
                "type": "Element",
                "max_length": 2,
            }
        )
        country_bank_number2: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber2",
                "type": "Element",
                "max_length": 2,
            }
        )
        country_bank_number3: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber3",
                "type": "Element",
                "max_length": 2,
            }
        )
        country_bank_number4: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber4",
                "type": "Element",
                "max_length": 2,
            }
        )
        country_bank_number5: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber5",
                "type": "Element",
                "max_length": 2,
            }
        )
        bank_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber",
                "type": "Element",
                "max_length": 30,
            }
        )
        bank_number2: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber2",
                "type": "Element",
                "max_length": 30,
            }
        )
        bank_number3: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber3",
                "type": "Element",
                "max_length": 30,
            }
        )
        bank_number4: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber4",
                "type": "Element",
                "max_length": 30,
            }
        )
        bank_number5: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber5",
                "type": "Element",
                "max_length": 30,
            }
        )
        country_bank_number_dom: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumberDom",
                "type": "Element",
                "max_length": 2,
            }
        )
        bank_number_dom: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumberDom",
                "type": "Element",
                "max_length": 30,
            }
        )
        account_central: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "AccountCentral",
                "type": "Element",
                "length": 0,
            }
        )
        customer_group: Optional[str] = field(
            default=None,
            metadata={
                "name": "CustomerGroup",
                "type": "Element",
                "max_length": 255,
            }
        )
        title: Optional[str] = field(
            default=None,
            metadata={
                "name": "Title",
                "type": "Element",
                "max_length": 30,
            }
        )
        free_field1: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField1",
                "type": "Element",
                "max_length": 255,
            }
        )
        free_field2: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField2",
                "type": "Element",
                "max_length": 255,
            }
        )
        due: Optional[Union[str, DueTypeValue]] = field(
            default=None,
            metadata={
                "name": "Due",
                "type": "Element",
                "length": 0,
            }
        )
        due_days: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "DueDays",
                "type": "Element",
                "length": 0,
            }
        )
        website: Optional[str] = field(
            default=None,
            metadata={
                "name": "Website",
                "type": "Element",
                "max_length": 50,
            }
        )
        intrastat_delivery: Optional[IntrastatDeliveryType] = field(
            default=None,
            metadata={
                "name": "IntrastatDelivery",
                "type": "Element",
            }
        )
        bic: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC",
                "type": "Element",
                "max_length": 12,
            }
        )
        bic2: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC2",
                "type": "Element",
                "max_length": 12,
            }
        )
        bic3: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC3",
                "type": "Element",
                "max_length": 12,
            }
        )
        bic4: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC4",
                "type": "Element",
                "max_length": 12,
            }
        )
        bic5: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC5",
                "type": "Element",
                "max_length": 12,
            }
        )
        bicdom: Optional[str] = field(
            default=None,
            metadata={
                "name": "BICDOM",
                "type": "Element",
                "max_length": 12,
            }
        )
        ventil: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Ventil",
                "type": "Element",
                "length": 0,
            }
        )
        memo: Optional[str] = field(
            default=None,
            metadata={
                "name": "MEMO",
                "type": "Element",
                "max_length": 255,
            }
        )
        discountperc: Optional[str] = field(
            default=None,
            metadata={
                "name": "DISCOUNTPERC",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        status: Optional[StatusType] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
            }
        )
        deliv_date: Optional[DelivDateType] = field(
            default=None,
            metadata={
                "name": "DelivDate",
                "type": "Element",
            }
        )
        date_payed: Optional[DatePayedType] = field(
            default=None,
            metadata={
                "name": "DatePayed",
                "type": "Element",
            }
        )
        elec_tb: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "ElecTb",
                "type": "Element",
                "length": 0,
            }
        )
        codadiscount_term: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "CODADiscountTerm",
                "type": "Element",
                "length": 0,
            }
        )


@dataclass
class FinDetailType:
    detail: List["FinDetailType.Detail"] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Detail:
        ventil: Optional[FinVentilType] = field(
            default=None,
            metadata={
                "name": "Ventil",
                "type": "Element",
                "required": True,
            }
        )
        account: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Account",
                "type": "Element",
                "length": 0,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        amount_acc: Optional[str] = field(
            default=None,
            metadata={
                "name": "AmountAcc",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Element",
                "max_length": 3,
            }
        )
        customer_prime: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Customer_Prime",
                "type": "Element",
                "length": 0,
            }
        )
        date: Optional[str] = field(
            default=None,
            metadata={
                "name": "Date",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        deb_cre: Optional[DebCreType] = field(
            default=None,
            metadata={
                "name": "DebCre",
                "type": "Element",
            }
        )
        doc_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "DocNumber",
                "type": "Element",
                "min_inclusive": 0,
                "max_inclusive": 999999999,
            }
        )
        doc_type: Optional[FinDocTypeType] = field(
            default=None,
            metadata={
                "name": "DocType",
                "type": "Element",
            }
        )
        rate: Optional[str] = field(
            default=None,
            metadata={
                "name": "Rate",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "Ref",
                "type": "Element",
                "max_length": 255,
            }
        )
        supplier_prime: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Supplier_Prime",
                "type": "Element",
                "length": 0,
            }
        )
        type_fin: Optional[Union[str, TypeFinTypeValue]] = field(
            default=None,
            metadata={
                "name": "TypeFin",
                "type": "Element",
            }
        )
        unit1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit1",
                "type": "Element",
            }
        )
        unit2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit2",
                "type": "Element",
            }
        )
        vat1: Optional[str] = field(
            default=None,
            metadata={
                "name": "VAT1",
                "type": "Element",
            }
        )
        vatproc: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "VATProc",
                "type": "Element",
                "length": 0,
            }
        )
        vat: Optional[str] = field(
            default=None,
            metadata={
                "name": "VAT",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        analytics1: Optional[AnalyticType] = field(
            default=None,
            metadata={
                "name": "Analytics1",
                "type": "Element",
            }
        )
        analytics2: Optional[AnalyticType] = field(
            default=None,
            metadata={
                "name": "Analytics2",
                "type": "Element",
            }
        )


@dataclass
class IscustomerType:
    class Meta:
        name = "ISCustomerType"

    iscustomer: List["IscustomerType.Iscustomer"] = field(
        default_factory=list,
        metadata={
            "name": "ISCustomer",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Iscustomer:
        account: Optional[int] = field(
            default=None,
            metadata={
                "name": "Account",
                "type": "Element",
                "required": True,
            }
        )
        doc_type: Optional[DocTypeType] = field(
            default=None,
            metadata={
                "name": "DocType",
                "type": "Element",
                "required": True,
            }
        )
        doc_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "DocNumber",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 999999999,
            }
        )
        doc_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DocDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        due_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DueDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Element",
                "max_length": 3,
            }
        )
        customer_prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Customer_Prime",
                "type": "Element",
                "required": True,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        discount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Discount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        vatamount: Optional[str] = field(
            default=None,
            metadata={
                "name": "VATAmount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        our_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "OurRef",
                "type": "Element",
                "max_length": 255,
            }
        )
        your_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "YourRef",
                "type": "Element",
                "max_length": 255,
            }
        )
        state: Optional[Union[str, StateTypeValue]] = field(
            default=None,
            metadata={
                "name": "State",
                "type": "Element",
                "length": 0,
            }
        )
        rate: Optional[str] = field(
            default=None,
            metadata={
                "name": "Rate",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        status: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )


@dataclass
class IssupplierType:
    class Meta:
        name = "ISSupplierType"

    issupplier: List["IssupplierType.Issupplier"] = field(
        default_factory=list,
        metadata={
            "name": "ISSupplier",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Issupplier:
        account: Optional[int] = field(
            default=None,
            metadata={
                "name": "Account",
                "type": "Element",
                "required": True,
            }
        )
        doc_type: Optional[DocTypeType] = field(
            default=None,
            metadata={
                "name": "DocType",
                "type": "Element",
                "required": True,
            }
        )
        doc_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "DocNumber",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 999999999,
            }
        )
        doc_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DocDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        due_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DueDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Element",
                "max_length": 3,
            }
        )
        supplier_prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Supplier_Prime",
                "type": "Element",
                "required": True,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        discount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Discount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        vatamount: Optional[str] = field(
            default=None,
            metadata={
                "name": "VATAmount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        our_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "OurRef",
                "type": "Element",
                "max_length": 255,
            }
        )
        your_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "YourRef",
                "type": "Element",
                "max_length": 255,
            }
        )
        state: Optional[Union[str, StateTypeValue]] = field(
            default=None,
            metadata={
                "name": "State",
                "type": "Element",
                "length": 0,
            }
        )
        rate: Optional[str] = field(
            default=None,
            metadata={
                "name": "Rate",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        status: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )


@dataclass
class IntrastatType:
    intrastat: List["IntrastatType.Intrastat"] = field(
        default_factory=list,
        metadata={
            "name": "Intrastat",
            "type": "Element",
        }
    )

    @dataclass
    class Intrastat:
        mass: Optional[str] = field(
            default=None,
            metadata={
                "name": "Mass",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        stat_units: Optional[str] = field(
            default=None,
            metadata={
                "name": "StatUnits",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        destination: Optional[str] = field(
            default=None,
            metadata={
                "name": "Destination",
                "type": "Element",
                "required": True,
                "max_length": 2,
            }
        )
        transport: Optional[TransportType] = field(
            default=None,
            metadata={
                "name": "Transport",
                "type": "Element",
            }
        )
        transaction: Optional[TransportType] = field(
            default=None,
            metadata={
                "name": "Transaction",
                "type": "Element",
            }
        )
        goodscode: Optional[str] = field(
            default=None,
            metadata={
                "name": "Goodscode",
                "type": "Element",
                "max_length": 8,
            }
        )
        region: Optional[RegionType] = field(
            default=None,
            metadata={
                "name": "Region",
                "type": "Element",
            }
        )
        delivery: Optional[IntrastatDeliveryType] = field(
            default=None,
            metadata={
                "name": "Delivery",
                "type": "Element",
            }
        )


@dataclass
class PurchaseDetailType:
    detail: List["PurchaseDetailType.Detail"] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Detail:
        account: Optional[int] = field(
            default=None,
            metadata={
                "name": "Account",
                "type": "Element",
                "required": True,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        deb_cre: Optional[DebCreType] = field(
            default=None,
            metadata={
                "name": "DebCre",
                "type": "Element",
                "required": True,
            }
        )
        ventil: Optional[int] = field(
            default=None,
            metadata={
                "name": "Ventil",
                "type": "Element",
                "required": True,
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "Ref",
                "type": "Element",
                "max_length": 255,
            }
        )
        unit1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit1",
                "type": "Element",
            }
        )
        unit2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit2",
                "type": "Element",
            }
        )
        vatproc: Optional[int] = field(
            default=None,
            metadata={
                "name": "VATProc",
                "type": "Element",
            }
        )
        type_aan: Optional[Union[str, TypeAanTypeValue]] = field(
            default=None,
            metadata={
                "name": "TypeAan",
                "type": "Element",
                "length": 0,
            }
        )
        vat1: Optional[str] = field(
            default=None,
            metadata={
                "name": "VAT1",
                "type": "Element",
            }
        )
        vat2: Optional[str] = field(
            default=None,
            metadata={
                "name": "VAT2",
                "type": "Element",
            }
        )
        vat3: Optional[str] = field(
            default=None,
            metadata={
                "name": "VAT3",
                "type": "Element",
            }
        )
        analytics1: Optional[AnalyticType] = field(
            default=None,
            metadata={
                "name": "Analytics1",
                "type": "Element",
            }
        )
        analytics2: Optional[AnalyticType] = field(
            default=None,
            metadata={
                "name": "Analytics2",
                "type": "Element",
            }
        )
        vat_refund_code: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "VatRefundCode",
                "type": "Element",
                "length": 0,
            }
        )
        vat_refund_sub_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "VatRefundSubCode",
                "type": "Element",
            }
        )
        vat_refund_text: Optional[str] = field(
            default=None,
            metadata={
                "name": "VatRefundText",
                "type": "Element",
            }
        )
        vat_refund_language: Optional[str] = field(
            default=None,
            metadata={
                "name": "VatRefundLanguage",
                "type": "Element",
            }
        )
        vat_refund_type: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "VatRefundType",
                "type": "Element",
                "length": 0,
            }
        )


@dataclass
class SaleDetailType:
    detail: List["SaleDetailType.Detail"] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Detail:
        account: Optional[int] = field(
            default=None,
            metadata={
                "name": "Account",
                "type": "Element",
                "required": True,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        deb_cre: Optional[DebCreType] = field(
            default=None,
            metadata={
                "name": "DebCre",
                "type": "Element",
                "required": True,
            }
        )
        ventil: Optional[int] = field(
            default=None,
            metadata={
                "name": "Ventil",
                "type": "Element",
                "required": True,
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "Ref",
                "type": "Element",
                "max_length": 255,
            }
        )
        unit1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit1",
                "type": "Element",
            }
        )
        unit2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit2",
                "type": "Element",
            }
        )
        vat1: Optional[str] = field(
            default=None,
            metadata={
                "name": "VAT1",
                "type": "Element",
            }
        )
        vatproc: Optional[str] = field(
            default=None,
            metadata={
                "name": "VATProc",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        mossdefault: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "MOSSDefault",
                "type": "Element",
                "length": 0,
            }
        )
        analytics1: Optional[AnalyticType] = field(
            default=None,
            metadata={
                "name": "Analytics1",
                "type": "Element",
            }
        )
        analytics2: Optional[AnalyticType] = field(
            default=None,
            metadata={
                "name": "Analytics2",
                "type": "Element",
            }
        )


@dataclass
class SundryDetailType:
    detail: List["SundryDetailType.Detail"] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Detail:
        ventil: Optional[SunVentilType] = field(
            default=None,
            metadata={
                "name": "Ventil",
                "type": "Element",
                "required": True,
            }
        )
        account: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Account",
                "type": "Element",
                "length": 0,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        amount_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "AmountRef",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Element",
                "max_length": 3,
            }
        )
        customer_prime: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Customer_Prime",
                "type": "Element",
                "length": 0,
            }
        )
        deb_cre: Optional[DebCreType] = field(
            default=None,
            metadata={
                "name": "DebCre",
                "type": "Element",
            }
        )
        doc_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "DocNumber",
                "type": "Element",
                "min_inclusive": 0,
                "max_inclusive": 999999999,
            }
        )
        doc_type: Optional[FinDocTypeType] = field(
            default=None,
            metadata={
                "name": "DocType",
                "type": "Element",
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "Ref",
                "type": "Element",
                "max_length": 255,
            }
        )
        supplier_prime: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Supplier_Prime",
                "type": "Element",
                "length": 0,
            }
        )
        type_div: Optional[Union[str, TypeDivTypeValue]] = field(
            default=None,
            metadata={
                "name": "TypeDiv",
                "type": "Element",
                "length": 0,
            }
        )
        unit1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit1",
                "type": "Element",
            }
        )
        unit2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit2",
                "type": "Element",
            }
        )
        analytics1: Optional[AnalyticType] = field(
            default=None,
            metadata={
                "name": "Analytics1",
                "type": "Element",
            }
        )
        analytics2: Optional[AnalyticType] = field(
            default=None,
            metadata={
                "name": "Analytics2",
                "type": "Element",
            }
        )


@dataclass
class SupplierType:
    supplier: List["SupplierType.Supplier"] = field(
        default_factory=list,
        metadata={
            "name": "Supplier",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Supplier:
        prime: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Prime",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        alfa: Optional[str] = field(
            default=None,
            metadata={
                "name": "Alfa",
                "type": "Element",
                "max_length": 10,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
                "max_length": 255,
            }
        )
        country: Optional[str] = field(
            default=None,
            metadata={
                "name": "Country",
                "type": "Element",
                "required": True,
                "max_length": 2,
            }
        )
        street: Optional[str] = field(
            default=None,
            metadata={
                "name": "Street",
                "type": "Element",
                "max_length": 60,
            }
        )
        house_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "HouseNumber",
                "type": "Element",
                "max_length": 10,
            }
        )
        mailbox_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "MailboxNumber",
                "type": "Element",
                "max_length": 5,
            }
        )
        zip_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ZipCode",
                "type": "Element",
                "max_length": 10,
            }
        )
        city: Optional[str] = field(
            default=None,
            metadata={
                "name": "City",
                "type": "Element",
                "max_length": 50,
            }
        )
        language: Optional[Union[str, LanguageTypeValue]] = field(
            default=None,
            metadata={
                "name": "Language",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Element",
                "required": True,
                "max_length": 3,
            }
        )
        vatcode: Optional[Union[str, VatcodeTypeValue]] = field(
            default=None,
            metadata={
                "name": "VATCode",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        vatstatus: Optional[Union[str, VatstatusTypeValue]] = field(
            default=None,
            metadata={
                "name": "VATStatus",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        vatnumber: Optional[str] = field(
            default=None,
            metadata={
                "name": "VATNumber",
                "type": "Element",
                "max_length": 30,
            }
        )
        extra1: Optional[str] = field(
            default=None,
            metadata={
                "name": "Extra1",
                "type": "Element",
                "max_length": 255,
            }
        )
        extra2: Optional[str] = field(
            default=None,
            metadata={
                "name": "Extra2",
                "type": "Element",
                "max_length": 255,
            }
        )
        extra3: Optional[str] = field(
            default=None,
            metadata={
                "name": "Extra3",
                "type": "Element",
                "max_length": 255,
            }
        )
        phone: Optional[str] = field(
            default=None,
            metadata={
                "name": "Phone",
                "type": "Element",
                "max_length": 30,
            }
        )
        fax: Optional[str] = field(
            default=None,
            metadata={
                "name": "Fax",
                "type": "Element",
                "max_length": 30,
            }
        )
        gsm: Optional[str] = field(
            default=None,
            metadata={
                "name": "GSM",
                "type": "Element",
                "max_length": 30,
            }
        )
        email: Optional[str] = field(
            default=None,
            metadata={
                "name": "Email",
                "type": "Element",
                "max_length": 50,
            }
        )
        account_purchase: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "AccountPurchase",
                "type": "Element",
                "length": 0,
            }
        )
        goods_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "GoodsCode",
                "type": "Element",
                "max_length": 8,
            }
        )
        intrastat_transport: Optional[IntrastatTransportType] = field(
            default=None,
            metadata={
                "name": "IntrastatTransport",
                "type": "Element",
            }
        )
        intrastat_transaction: Optional[IntrastatTransportType] = field(
            default=None,
            metadata={
                "name": "IntrastatTransaction",
                "type": "Element",
            }
        )
        intrastat_delivery: Optional[IntrastatDeliveryType] = field(
            default=None,
            metadata={
                "name": "IntrastatDelivery",
                "type": "Element",
            }
        )
        country_bank_number1: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber1",
                "type": "Element",
                "max_length": 2,
            }
        )
        bank_number1: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber1",
                "type": "Element",
                "max_length": 34,
            }
        )
        country_bank_number2: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber2",
                "type": "Element",
                "max_length": 2,
            }
        )
        bank_number2: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber2",
                "type": "Element",
                "max_length": 34,
            }
        )
        country_bank_number3: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber3",
                "type": "Element",
                "max_length": 2,
            }
        )
        bank_number3: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber3",
                "type": "Element",
                "max_length": 34,
            }
        )
        country_bank_number4: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber4",
                "type": "Element",
                "max_length": 2,
            }
        )
        bank_number4: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber4",
                "type": "Element",
                "max_length": 34,
            }
        )
        country_bank_number5: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryBankNumber5",
                "type": "Element",
                "max_length": 2,
            }
        )
        bank_number5: Optional[str] = field(
            default=None,
            metadata={
                "name": "BankNumber5",
                "type": "Element",
                "max_length": 34,
            }
        )
        title: Optional[str] = field(
            default=None,
            metadata={
                "name": "Title",
                "type": "Element",
                "max_length": 30,
            }
        )
        website: Optional[str] = field(
            default=None,
            metadata={
                "name": "Website",
                "type": "Element",
                "max_length": 50,
            }
        )
        country_vatnumber: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryVATNumber",
                "type": "Element",
                "max_length": 2,
            }
        )
        ventil: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Ventil",
                "type": "Element",
                "length": 0,
            }
        )
        vattarif: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "VATTarif",
                "type": "Element",
                "length": 0,
            }
        )
        account_central: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "AccountCentral",
                "type": "Element",
                "length": 0,
            }
        )
        due: Optional[Union[str, DueTypeValue]] = field(
            default=None,
            metadata={
                "name": "Due",
                "type": "Element",
                "length": 0,
            }
        )
        due_days: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "DueDays",
                "type": "Element",
                "length": 0,
            }
        )
        supplier_group: Optional[str] = field(
            default=None,
            metadata={
                "name": "SupplierGroup",
                "type": "Element",
                "max_length": 255,
            }
        )
        free_field1: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField1",
                "type": "Element",
                "max_length": 255,
            }
        )
        free_field2: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeField2",
                "type": "Element",
                "max_length": 255,
            }
        )
        bic1: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC1",
                "type": "Element",
                "max_length": 12,
            }
        )
        bic2: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC2",
                "type": "Element",
                "max_length": 12,
            }
        )
        bic3: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC3",
                "type": "Element",
                "max_length": 12,
            }
        )
        bic4: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC4",
                "type": "Element",
                "max_length": 12,
            }
        )
        bic5: Optional[str] = field(
            default=None,
            metadata={
                "name": "BIC5",
                "type": "Element",
                "max_length": 12,
            }
        )
        memo: Optional[str] = field(
            default=None,
            metadata={
                "name": "MEMO",
                "type": "Element",
                "max_length": 255,
            }
        )
        discountperc: Optional[str] = field(
            default=None,
            metadata={
                "name": "DISCOUNTPERC",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        card: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "CARD",
                "type": "Element",
                "length": 0,
            }
        )
        status: Optional[StatusType] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
            }
        )
        dom: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Dom",
                "type": "Element",
                "length": 0,
            }
        )
        deliv_date: Optional[DelivDateType] = field(
            default=None,
            metadata={
                "name": "DelivDate",
                "type": "Element",
            }
        )
        date_payed: Optional[DatePayedType] = field(
            default=None,
            metadata={
                "name": "DatePayed",
                "type": "Element",
            }
        )
        vat_refund_code: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "VatRefundCode",
                "type": "Element",
                "length": 0,
            }
        )
        vat_refund_sub_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "VatRefundSubCode",
                "type": "Element",
            }
        )
        vat_refund_text: Optional[str] = field(
            default=None,
            metadata={
                "name": "VatRefundText",
                "type": "Element",
            }
        )
        vat_refund_language: Optional[str] = field(
            default=None,
            metadata={
                "name": "VatRefundLanguage",
                "type": "Element",
            }
        )
        vat_refund_type: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "VatRefundType",
                "type": "Element",
                "length": 0,
            }
        )
        codadiscount_term: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "CODADiscountTerm",
                "type": "Element",
                "length": 0,
            }
        )


@dataclass
class FinancialType:
    financial: List["FinancialType.Financial"] = field(
        default_factory=list,
        metadata={
            "name": "Financial",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Financial:
        journal_prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Journal_Prime",
                "type": "Element",
            }
        )
        year_alfa: Optional[int] = field(
            default=None,
            metadata={
                "name": "Year_Alfa",
                "type": "Element",
            }
        )
        doc_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "DocNumber",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 999999999,
            }
        )
        accounting_period: Optional[int] = field(
            default=None,
            metadata={
                "name": "AccountingPeriod",
                "type": "Element",
            }
        )
        vatmonth: Optional[int] = field(
            default=None,
            metadata={
                "name": "VATMonth",
                "type": "Element",
            }
        )
        doc_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DocDate",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        opening_balance: Optional[str] = field(
            default=None,
            metadata={
                "name": "OpeningBalance",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        final_balance: Optional[str] = field(
            default=None,
            metadata={
                "name": "FinalBalance",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        annex: Optional[str] = field(
            default=None,
            metadata={
                "name": "Annex",
                "type": "Element",
                "max_length": 255,
            }
        )
        details: Optional[FinDetailType] = field(
            default=None,
            metadata={
                "name": "Details",
                "type": "Element",
                "required": True,
            }
        )
        status: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )


@dataclass
class PurchaseType:
    purchase: List["PurchaseType.Purchase"] = field(
        default_factory=list,
        metadata={
            "name": "Purchase",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Purchase:
        journal_prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Journal_Prime",
                "type": "Element",
                "required": True,
            }
        )
        year_alfa: Optional[int] = field(
            default=None,
            metadata={
                "name": "Year_Alfa",
                "type": "Element",
                "required": True,
            }
        )
        doc_type: Optional[DocTypeType] = field(
            default=None,
            metadata={
                "name": "DocType",
                "type": "Element",
                "required": True,
            }
        )
        doc_state: Optional[DocStateType] = field(
            default=None,
            metadata={
                "name": "DocState",
                "type": "Element",
            }
        )
        supplier_prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Supplier_Prime",
                "type": "Element",
                "required": True,
            }
        )
        doc_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "DocNumber",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 999999999,
            }
        )
        accounting_period: Optional[int] = field(
            default=None,
            metadata={
                "name": "AccountingPeriod",
                "type": "Element",
            }
        )
        vatmonth: Optional[int] = field(
            default=None,
            metadata={
                "name": "VATMonth",
                "type": "Element",
            }
        )
        doc_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DocDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        due_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DueDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        our_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "OurRef",
                "type": "Element",
                "max_length": 255,
            }
        )
        your_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "YourRef",
                "type": "Element",
                "max_length": 255,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        discount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Discount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        ventil: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Ventil",
                "type": "Element",
                "length": 0,
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Element",
                "max_length": 3,
            }
        )
        rate: Optional[str] = field(
            default=None,
            metadata={
                "name": "Rate",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        vatamount: Optional[str] = field(
            default=None,
            metadata={
                "name": "VATAmount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        ogm: Optional[str] = field(
            default=None,
            metadata={
                "name": "OGM",
                "type": "Element",
                "max_length": 255,
            }
        )
        annex: Optional[str] = field(
            default=None,
            metadata={
                "name": "Annex",
                "type": "Element",
                "max_length": 255,
            }
        )
        deliv_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DelivDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        date_payed: Optional[str] = field(
            default=None,
            metadata={
                "name": "DatePayed",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        pay_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "PayDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        pay_cash: Optional[int] = field(
            default=None,
            metadata={
                "name": "PayCash",
                "type": "Element",
            }
        )
        details: Optional[PurchaseDetailType] = field(
            default=None,
            metadata={
                "name": "Details",
                "type": "Element",
                "required": True,
            }
        )
        intrastats: Optional[IntrastatType] = field(
            default=None,
            metadata={
                "name": "Intrastats",
                "type": "Element",
            }
        )
        status: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )


@dataclass
class SaleType:
    sale: List["SaleType.Sale"] = field(
        default_factory=list,
        metadata={
            "name": "Sale",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Sale:
        journal_prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Journal_Prime",
                "type": "Element",
            }
        )
        year_alfa: Optional[int] = field(
            default=None,
            metadata={
                "name": "Year_Alfa",
                "type": "Element",
            }
        )
        doc_type: Optional[DocTypeType] = field(
            default=None,
            metadata={
                "name": "DocType",
                "type": "Element",
                "required": True,
            }
        )
        doc_state: Optional[DocStateType] = field(
            default=None,
            metadata={
                "name": "DocState",
                "type": "Element",
            }
        )
        customer_prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Customer_Prime",
                "type": "Element",
                "required": True,
            }
        )
        doc_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "DocNumber",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 999999999,
            }
        )
        accounting_period: Optional[int] = field(
            default=None,
            metadata={
                "name": "AccountingPeriod",
                "type": "Element",
            }
        )
        vatmonth: Optional[int] = field(
            default=None,
            metadata={
                "name": "VATMonth",
                "type": "Element",
            }
        )
        doc_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DocDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        due_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DueDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        our_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "OurRef",
                "type": "Element",
                "max_length": 255,
            }
        )
        your_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "YourRef",
                "type": "Element",
                "max_length": 255,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        discount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Discount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        ventil: Optional[Union[int, str]] = field(
            default=None,
            metadata={
                "name": "Ventil",
                "type": "Element",
                "length": 0,
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Element",
                "max_length": 3,
            }
        )
        rate: Optional[str] = field(
            default=None,
            metadata={
                "name": "Rate",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        vatamount: Optional[str] = field(
            default=None,
            metadata={
                "name": "VATAmount",
                "type": "Element",
                "min_length": 1,
                "max_length": 20,
                "pattern": r"[\-+]?[0-9]{1,14}[,.]?[0-9]{0,4}",
            }
        )
        ogm: Optional[str] = field(
            default=None,
            metadata={
                "name": "OGM",
                "type": "Element",
                "max_length": 255,
            }
        )
        annex: Optional[str] = field(
            default=None,
            metadata={
                "name": "Annex",
                "type": "Element",
                "max_length": 255,
            }
        )
        details: Optional[SaleDetailType] = field(
            default=None,
            metadata={
                "name": "Details",
                "type": "Element",
                "required": True,
            }
        )
        intrastats: Optional[IntrastatType] = field(
            default=None,
            metadata={
                "name": "Intrastats",
                "type": "Element",
            }
        )
        status: Optional[Union[str, BoolTypeValue]] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
                "length": 0,
            }
        )
        deliv_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DelivDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        date_payed: Optional[str] = field(
            default=None,
            metadata={
                "name": "DatePayed",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        pay_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "PayDate",
                "type": "Element",
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        pay_cash: Optional[int] = field(
            default=None,
            metadata={
                "name": "PayCash",
                "type": "Element",
            }
        )


@dataclass
class SundryType:
    sundry: List["SundryType.Sundry"] = field(
        default_factory=list,
        metadata={
            "name": "Sundry",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Sundry:
        journal_prime: Optional[int] = field(
            default=None,
            metadata={
                "name": "Journal_Prime",
                "type": "Element",
            }
        )
        year_alfa: Optional[int] = field(
            default=None,
            metadata={
                "name": "Year_Alfa",
                "type": "Element",
            }
        )
        doc_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "DocNumber",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 999999999,
            }
        )
        accounting_period: Optional[int] = field(
            default=None,
            metadata={
                "name": "AccountingPeriod",
                "type": "Element",
            }
        )
        vatmonth: Optional[int] = field(
            default=None,
            metadata={
                "name": "VATMonth",
                "type": "Element",
            }
        )
        doc_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DocDate",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
            }
        )
        annex: Optional[str] = field(
            default=None,
            metadata={
                "name": "Annex",
                "type": "Element",
                "max_length": 255,
            }
        )
        details: Optional[SundryDetailType] = field(
            default=None,
            metadata={
                "name": "Details",
                "type": "Element",
                "required": True,
            }
        )
        status: Optional[StatusType] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class ImportExpMplusType:
    class Meta:
        name = "ImportExpMPlusType"

    customers: Optional[CustomerType] = field(
        default=None,
        metadata={
            "name": "Customers",
            "type": "Element",
        }
    )
    suppliers: Optional[SupplierType] = field(
        default=None,
        metadata={
            "name": "Suppliers",
            "type": "Element",
        }
    )
    accounts: Optional[AccountType] = field(
        default=None,
        metadata={
            "name": "Accounts",
            "type": "Element",
        }
    )
    analytic_accounts: Optional[AnalyticAccountType] = field(
        default=None,
        metadata={
            "name": "AnalyticAccounts",
            "type": "Element",
        }
    )
    iscustomers: Optional[IscustomerType] = field(
        default=None,
        metadata={
            "name": "ISCustomers",
            "type": "Element",
        }
    )
    issuppliers: Optional[IssupplierType] = field(
        default=None,
        metadata={
            "name": "ISSuppliers",
            "type": "Element",
        }
    )
    sales: Optional[SaleType] = field(
        default=None,
        metadata={
            "name": "Sales",
            "type": "Element",
        }
    )
    purchases: Optional[PurchaseType] = field(
        default=None,
        metadata={
            "name": "Purchases",
            "type": "Element",
        }
    )
    sundries: Optional[SundryType] = field(
        default=None,
        metadata={
            "name": "Sundries",
            "type": "Element",
        }
    )
    financials: Optional[FinancialType] = field(
        default=None,
        metadata={
            "name": "Financials",
            "type": "Element",
        }
    )


@dataclass
class ImportExpMplus(ImportExpMplusType):
    class Meta:
        name = "ImportExpMPlus"
