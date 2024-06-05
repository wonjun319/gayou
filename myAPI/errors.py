from requests import Response
from typing import Dict, Any, Callable

__all__ = [
    "CreateAskError",
    "CreateBidError",
    "InsufficientFundsAsk",
    "InsufficientFundsBid",
    "UnderMinTotalAsk",
    "UnderMinTotalBid",
    "WidthdrawAddressNotRegisterd",
    "ValidationError",
    "InvalidQueryPayload",
    "JwtVerification",
    "ExpiredAccessKey",
    "NonceUsed",
    "NoAutorizationIP",
    "OutOfScope",
    "TooManyRequests",
    "RemainingReqParsingError",
    "InValidAccessKey",
    "error_handler",  # raise_error must be in place of last in this list
]


class ErrorMixin(Exception):
    name: str
    code: int
    msg: str

    def __init__(self, **ctx: Any) -> None:
        self.__dict__ = ctx

    def __str__(self) -> str:
        return self.msg.format(**self.__dict__)


class Error(ErrorMixin):
    pass


class BadRequestError(ErrorMixin):
    pass


class UnauthorizedError(ErrorMixin):
    pass


class CreateAskError(BadRequestError):
    name = "create_ask_error"
    code = 400
    msg = "주문 요청 정보가 올바르지 않습니다."


class CreateBidError(BadRequestError):
    name = "create_bid_error"
    code = 400
    msg = "주문 요청 정보가 올바르지 않습니다."


class InsufficientFundsAsk(BadRequestError):
    name = "insufficient_funds_ask"
    code = 400
    msg = "매수/매도 가능 잔고가 부족합니다."


class InsufficientFundsBid(BadRequestError):
    name = "insufficient_funds_bid"
    code = 400
    msg = "매수/매도 가능 잔고가 부족합니다."


class UnderMinTotalAsk(BadRequestError):
    name = "under_min_total_ask"
    code = 400
    msg = "주문 요청 금액이 최소 주문 금액 미만입니다."


class UnderMinTotalBid(BadRequestError):
    name = "under_min_total_bid"
    code = 400
    msg = "주문 요청 금액이 최소 주문 금액 미만입니다."


class WidthdrawAddressNotRegisterd(BadRequestError):
    name = "withdraw_address_not_registerd"
    code = 400
    msg = "허용되지 않은 출금 주소입니다."


class ValidationError(BadRequestError):
    name = "validation_error"
    code = 400
    msg = "잘못된 API 요청입니다."


class InvalidQueryPayload(UnauthorizedError):
    name = "invalid_query_payload"
    code = 401
    msg = "JWT 헤더의 페이로드가 올바르지 않습니다."


class JwtVerification(UnauthorizedError):
    name = "jwt_verification"
    code = 401
    msg = "JWT 토큰 검증에 실패했습니다."


class ExpiredAccessKey(UnauthorizedError):
    name = "expired_access_key"
    code = 401
    msg = "API 키가 만료되었습니다."


class NonceUsed(UnauthorizedError):
    name = "nonce_used"
    code = 401
    msg = "이미 요청한 nonce값이 다시 사용되었습니다."


class NoAutorizationIP(UnauthorizedError):
    name = "no_authorization_i_p"
    code = 401
    msg = "허용되지 않은 IP 주소입니다."


class OutOfScope(UnauthorizedError):
    name = "out_of_scope"
    code = 401
    msg = "허용되지 않은 기능입니다."


class InValidAccessKey(UnauthorizedError):
    name = ""
    code = -1
    msg = "잘못된 엑세스 키입니다."


INVALID_REQUEST_PARAMETER_ERROR = [eval(err) for err in __all__[:-1] if eval(err).code == '10']
NO_MANDATORY_REQUEST_PARAMETERS_ERROR = [eval(err) for err in __all__[:-1] if eval(err).code == '11']
TEMPORARILY_DISABLE_THE_SERVICEKEY_ERROR = [eval(err) for err in __all__[:-1] if eval(err).code == '21']
UNSIGNED_CALL_ERROR = [eval(err) for err in __all__[:-1] if eval(err).code == '33']
NORMAL_CODE = [eval(err) for err in __all__[:-1] if eval(err).code == '00']
SERVICETIMEOUT_ERROR = [eval(err) for err in __all__[:-1] if eval(err).code == '05']
NODATA_ERROR = [eval(err) for err in __all__[:-1] if eval(err).code == '03']
DB_ERROR = [eval(err) for err in __all__[:-1] if eval(err).code == '02']


def error_handler(func: Callable):
    def wrapper(*args: Any, **kwargs: Dict[str, Any]) -> Response:
        message, name = "", ""

        resp = func(*args, **kwargs)
        if resp.ok:
            return resp

        error = resp.json().get("error", {})
        if bool(error):
            message = error.get("message")
            name = error.get("name")

        code = resp.status_code
        if code == 10:
            for err in INVALID_REQUEST_PARAMETER_ERROR:
                if err.name == name:
                    raise err
        elif code == 11:
            for err in NO_MANDATORY_REQUEST_PARAMETERS_ERROR:
                if err.name == name:
                    raise err
        elif code == 21:
            for err in TEMPORARILY_DISABLE_THE_SERVICEKEY_ERROR:
                if err.name == name:
                    raise err
        elif code == 33:
            for err in UNSIGNED_CALL_ERROR:
                if err.name == name:
                    raise err
        else:
            raise Error(name=name, code=code, msg=message)
        return resp
    return wrapper
