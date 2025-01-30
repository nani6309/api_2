from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Empdetails
from . serializers import empdetailsserializer

# Create your views here.


@api_view(['GET'])
def getemp(request):
    Employee = Empdetails.objects.all()
    serializer =  empdetailsserializer(Employee,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addemp(request):
    newemp = request.data
    serializer = empdetailsserializer(data=newemp,many = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)




@api_view(['GET','POST','PUT','PATCH'])
def addview(request):
    if request.method == 'GET':
        Employee = Empdetails.objects.all()
        serializer =  empdetailsserializer(Employee,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        newemp = request.data
        serializer = empdetailsserializer(data=newemp,many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PUT":
        newdata = request.data
        employee = Empdetails.objects.get(id = newdata['id'])
        serializer = empdetailsserializer(employee,data=newdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        newdata = request.data
        employee = Empdetails.objects.get(id = newdata['id'])
        serializer = empdetailsserializer(employee,data=newdata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        newdata = request.data
        employee = Empdetails.objects.get(id = newdata['id'])
        employee.delete()
        return Response({'message': 'Person deleted'})
    

@api_view(['DELETE'])
def deleteEmployee(request, pk):
        # Attempt to get the employee by pk
        employee = Empdetails.objects.get(id=pk)
        employee.delete()  # Delete the employee
        return Response({"message": "Employee deleted successfully"})
