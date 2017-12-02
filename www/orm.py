import asyncio,logging
import aiomysql


@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database conntion pool....')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommnit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )

@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
