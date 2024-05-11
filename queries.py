Issue.objects.filter(status__name='Finished', updated_at__gte=(datetime.now() - timedelta(days=30)))

Issue.objects.filter(status__name__in=['New', 'Accepted'], type__name__in=['Bug', 'Task'])

Issue.objects.filter(summary__icontains='bug', type__name='Bug').exclude(status__name='Finished')
Issue.objects.filter(~Q(status__name='Finished'), summary__icontains='bug', type__name='Bug')

Issue.objects.values('id', 'summary', 'type', 'status')
Issue.objects.values_list('id', 'summary', 'type', 'status')

Issue.objects.filter(summary=F('description'))

Issue.objects.filter(type__name='Task').count()

Issue.objects.filter(type__name='Bug').count()

Issue.objects.filter(type__name='Enhancement').count()
