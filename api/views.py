from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import Student
from .serializers import StudentSerializer
from django.db.models.functions import Lower


# Create your views here.

@api_view(["GET", "POST"])
def student_list_create(request):
    if request.method == "GET":
        students = Student.objects.all().order_by(Lower("name"))
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, student_id):
    # Find the student or return 404.
    student = get_object_or_404(Student, pk=student_id)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
        # Serialize and return one student.

    if request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Validate request.data against the existing instance.
        # Return the updated object or validation errors.
        
    deleted_id = str(student.id)
    student.delete()
    return Response({"message": "Student deleted.", "_id": deleted_id})
    # Save the ID as a string, delete the instance, and return JSON.
