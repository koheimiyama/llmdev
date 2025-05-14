import pytest
from authenticator import Authenticator


@pytest.fixture
def authenticator():
    auth = Authenticator()
    auth.register("user1", "pass1")
    return auth


def test_register_normal(authenticator):
    assert "user1" in authenticator.users


def test_register_error(authenticator):
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register("user1", "pass1")


def test_login_normal(authenticator):
    result = authenticator.login("user1", "pass1")
    assert "ログイン成功" == result


def test_login_error(authenticator):
    with pytest.raises(
        ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"
    ):
        authenticator.login("user1", "passng")
