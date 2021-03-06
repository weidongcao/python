#!/usr/bin/python
#coding=utf-8

EMAIL_SELECT_RUNNING = """select
    run_id,
    conf_id,
    email_id,
    attachment_name,
    temple_path,
    picture_name,
    email_theme,
    email_content_convert,
    email_content_type,
    email_content_encode,
    email_content_col,
    sender_email,
    sender_name,
    email_server,
    server_port,
    receiver_list,
    run_status,
    create_date,
    update_date
from
    running_email_info
where
    run_status = 0"""

EMAIL_UPDATE_RUNNING = """
update running_email_info set run_status = {run_status}, update_date = NOW() where run_id = {run_id};
"""
EMAIL_SELECT_SENDER = """
select sender_passwd from config_sender_info sender LEFT JOIN config_email_conf conf on sender.sender_id = conf.sender_id where conf.conf_id = {conf_id};
"""
