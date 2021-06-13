import sys

import celery
import memory 
import cpu 

from celery.utils.log import get_task_logger


celery_app = celery.Celery()
celery_app.config_from_object('celery_config')

@celery_app.task(name='loadsamemory', ignore_result=True)
def loadsamemory():
    logger = get_task_logger('loadsamemory')
    logger.info("loadsa memory!")
    memory.eatmemory()

@celery_app.task(name='loadsacpu', ignore_result=True)
def loadsacpu():
    logger = get_task_logger('loadsacpu')
    logger.info("loadsa cpu!")
    cpu.eatcpu()

