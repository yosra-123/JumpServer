# -*- coding: utf-8 -*-
#
from django.urls import path

from rest_framework_bulk.routes import BulkRouter

from .. import api

app_name = 'tickets'
router = BulkRouter()

router.register('tickets', api.TicketViewSet, 'ticket')
router.register('apply-asset-tickets', api.ApplyAssetTicketViewSet, 'apply-asset-ticket')
router.register('apply-app-tickets', api.ApplyApplicationTicketViewSet, 'apply-app-ticket')
router.register('apply-login-tickets', api.ApplyLoginTicketViewSet, 'apply-login-ticket')
router.register('apply-login-asset-tickets', api.ApplyLoginAssetTicketViewSet, 'apply-login-asset-ticket')
router.register('apply-command-tickets', api.ApplyCommandTicketViewSet, 'apply-command-ticket')
router.register('flows', api.TicketFlowViewSet, 'flows')
router.register('comments', api.CommentViewSet, 'comment')
router.register('ticket-session-relation', api.TicketSessionRelationViewSet, 'ticket-session-relation')

urlpatterns = [
    path('tickets/<uuid:ticket_id>/session/', api.TicketSessionApi.as_view(), name='ticket-sesion'),
    path('super-tickets/<uuid:pk>/status/', api.SuperTicketStatusAPI.as_view(), name='super-ticket-status'),
]
urlpatterns += router.urls