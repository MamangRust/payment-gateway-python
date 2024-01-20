import logging
from config.sqlite import SQLiteConnection
from repository.main import Repository

from service.user import UserService
from service.saldo import SaldoService
from service.topup import TopupService
from service.withdraw import WithdrawService
from service.transfer import TransferService


db_connection = SQLiteConnection('database.db')

repository = Repository(db_connection)

user_service = UserService(repository.user_repository, repository.saldo_repository)
saldo_service = SaldoService(repository.saldo_repository)
topup_service = TopupService(repository.topup_repository, repository.saldo_repository)


withdraw_service = WithdrawService(repository.withdraw_repository, repository.saldo_repository)
transfer_service = TransferService(repository.transfer_repository, repository.saldo_repository)


# new_user = user_service.create_user("JmD9r@example.com", "password", "12333")


def users_all_service():
    all_users = user_service.get_all_users()
    create_user_by_email = user_service.create_user("JmD9r@example.com", "password", "12333")
    create_user = user_service.create_user("yanto@example.com", "password", "12333")
    user_by_email = user_service.get_user_by_email("yanto@example.com")
    user_by_id = user_service.get_user_by_id(user_by_email.user_id)
    updated_user = user_service.update_user(user_by_email.user_id, new_noc_transfer=12333)
    # delete_user = user_service.delete_user(user_by_email.user_id)


    print("New User:", create_user)
    print("User by Email:", user_by_email)
    print("User by ID:", user_by_id)
    print("Updated User:", updated_user)
    print("All Users:", str(all_users))
    # print("Delete User: " + str(delete_user))

    return user_by_email.user_id


def saldo_all_service(user_id: int):
    all_saldo = saldo_service.get_all_saldos()
    get_saldo_userId  = saldo_service.get_saldo_by_user_id(user_id)
    # create_saldo_1 = saldo_service.create_saldo(1, 100000, withdraw_amount=0, withdraw_time=None)
    create_saldo = saldo_service.create_saldo(user_id, 100000, withdraw_amount=0, withdraw_time=None)
    update_saldo = saldo_service.update_saldo(1, 200000)
    # delete_saldo = saldo_service.delete_saldo(user_id)


    print("All Saldo:", all_saldo)
    print("Get Saldo User ID:", get_saldo_userId)
    print("Create Saldo:", create_saldo)
    print("Update Saldo:", update_saldo)
    # print("Delete Saldo:", delete_saldo)


def topup_all_service(user_id: int):
    topup_amount = 100000
    topup_method = "BCA"
    topup = topup_service.create_topup(user_id, 100001,topup_amount, topup_method)
    topup_by_id = topup_service.get_topup_id(topup_id=topup.topup_id)
    topup_by_userId = topup_service.get_topup_by_user_id(user_id)
    all_topup = topup_service.get_all_topups()
    update_topup = topup_service.update_topup(topup_id=topup.topup_id, new_topup_amount=200000, new_topup_method="OVO")
    # delete_topup = topup_service.delete_topup(topup.topup_id)

    print("create topup: ", topup)
    print("topup by id: ", topup_by_id)
    print("topup by user id: ", topup_by_userId)
    print("all topup: ", all_topup)
    print("update topup: ", update_topup)
    # print("delete topup: ", delete_topup)


def transfer_all_service(user_id: int):
    create_transfer = transfer_service.create_transfer(1, 2, 100)
    get_all_transfer = transfer_service.get_all_transfers()
    get_transfer_by_userId = transfer_service.get_transfer_by_user_id(user_id)
    update_transfer = transfer_service.update_transfer(1, 200)
    delete_transfer = transfer_service.delete_transfer(1)

    print("create transfer: ", create_transfer)
    print("get all transfer: ", get_all_transfer)
    print("get transfer by user id: ", get_transfer_by_userId)
    print("update transfer: ", update_transfer)
    # print("delete transfer: ", delete_transfer)


def withdraw_all_service(user_id: int):
    withdraw_amount = 100000
    withdraw = withdraw_service.create_withdraw(user_id, withdraw_amount)
    withdraw_by_id = withdraw_service.get_withdraw_by_id(withdraw_id=withdraw.withdraw_id)
    withdraw_by_userId = withdraw_service.get_withdraw_by_user_id(user_id)
    all_withdraw = withdraw_service.get_all_withdraws()
    update_withdraw = withdraw_service.update_withdraw(withdraw_id=withdraw.withdraw_id, new_withdraw_amount=100)
    # delete_withdraw = withdraw_service.delete_withdraw(withdraw.withdraw_id)

    print("create withdraw: ", withdraw)
    print("withdraw by id: ", withdraw_by_id)
    print("withdraw by user id: ", withdraw_by_userId)
    print("all withdraw: ", all_withdraw)
    print("update withdraw: ", update_withdraw)
    # print("delete withdraw: ", delete_withdraw)

users_all_service()
saldo_all_service(user_id=2)
topup_all_service(user_id=2)

transfer_all_service(user_id=2)

withdraw_all_service(user_id=2)