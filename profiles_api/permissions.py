from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
      """Allow users to edit their own profile"""
      def has_object_permission(self, request, view, obj):
            """Check user is trying to edit their own profile"""
            # The safe methods are methods that don't require or don't make any changes
            # to the object. For instance, HTTP GET as you are reading the object, and
            # not actually trying to make any changes to the object itself.

            # We want to allow users to view other user profiles, but only be able to make
            # changes to their own profile.
            if request.method in permissions.SAFE_METHODS:
                  return True
            
            # This case handles if the request is not in SAFE_METHODS i.e. HTTP PUT to update an object.
            return obj.id == request.user.id    