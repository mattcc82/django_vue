from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from jobs.models import Job
from jobs.api.serializers import JobSerializer


class JobListAPIView(APIView):

    def get(self, request):
        jobs = Job.objects.filter(available=True)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailAPIView(APIView):

    def get_data(self, pk):
        job = get_object_or_404(Job, pk=pk)
        return job
    
    def get(self, request, pk):
        job = self.get_data(pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    def put(self, request, pk):
        job = self.get_data(pk)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        job = self.get_data(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
