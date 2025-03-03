from rest_framework.permissions import BasePermission


class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_instructor


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_student


class IsInstructorOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.instructor_id


class IsInstructorExamOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.exam.instructor_id
