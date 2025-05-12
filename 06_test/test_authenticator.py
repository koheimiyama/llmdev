import pytest
from authenticator import Authenticator


def test_register():
    auth = Authenticator()
    auth.register(username="user1", password="pass1")
    assert "user1" in auth.users
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        auth.register("user1", "pass1")


def test_login():
    auth = Authenticator()
    auth.register(username="user1", password="pass1")
    result = auth.login("user1", "pass1")
    assert "ログイン成功" == result
    with pytest.raises(
        ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"
    ):
        auth.login("user1", "passng")
