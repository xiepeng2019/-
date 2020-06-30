#coding=utf-8
import pytest, logging
from tsms_pytest_commons.tsms_base import TsmsBase
from tsms_pytest_commons.tsms_web import TsmsWeb
from tsms_pytest_commons.tsms_db import TsmsDB
from tsms_pytest_commons.tsms_rds import TsmsRedis

logger = logging.getLogger(__name__)


@pytest.fixture()
def login():
    logging.info("login 执行")
# E:\test_tsms_project\test_tsms_api\conftest.py

@pytest.fixture(scope="function")
def tb():
    return TsmsBase()


@pytest.fixture()
def td():
    return TsmsDB()


@pytest.fixture()
def tw():
    return TsmsWeb()


@pytest.fixture()

def rds():
    return TsmsRedis()


@pytest.fixture(scope="session")
def web_session():
    return TsmsWeb().get_web_session()


@pytest.fixture(scope="session")
def clear_sign_all():
    """
    统计sign_id，最后统一清理
    """
    pytest.sign_ids = []
    yield
    sign_ids = pytest.sign_ids
    if not sign_ids:
        logger.info("[当前sign_id列表为]: {} 不需要清理".format(sign_ids))
        return
    logger.info("[经过一轮测试，新增的sign_id是]: {}".format(sign_ids))
    try:
        ts = TsmsBase()
        for sign_id in sign_ids:
            ts.req_delete("sign", {"sign_id": sign_id})
            if ts.status_code != 200:
                logger.error("[签名删除失败，签名id为]：{}".format(sign_id))
    except Exception as e:
        logger.error(e)


@pytest.fixture(scope="function")
def clear_sign():
    """
    指定sign_id进行清理
    """

    def _clear_sign(sign_id):
        logger.info("[将要删除的sign_id是]: {}".format(sign_id))
        try:
            ts = TsmsBase()
            ts.req_delete("sign", {"sign_id": sign_id})
            if ts.status_code != 200:
                logger.warning("[签名删除失败，签名id为]：{}".format(sign_id))
            return ts.status_code
        except Exception as e:
            logger.error(e)

    return _clear_sign


@pytest.fixture()
def create_sign():
    """创建一个新签名"""
    tb = TsmsBase()
    data = tb.sign_data()
    tb.req_post("sign", data)
    return tb.json.get("sign_id")


@pytest.fixture()
def rejected_sign():
    """创建一个新签名，并审核为rejected"""
    tb = TsmsBase()
    data = tb.sign_data()
    tb.req_post("sign", data)
    sign_id = tb.json.get("sign_id")
    tb.review("sign", sign_id, audit_status="rejected")
    return sign_id
