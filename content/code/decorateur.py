#!/usr/bin/python
import objc

########################################################################
#                             Le décorateur                            #
########################################################################

def swizzle(*args):
    """
    Decorator to override an ObjC selector's implementation with a
    custom implementation ("method swizzling").

    Use like this:

    @swizzle(NSOriginalClass, 'selectorName')
    def swizzled_selectorName(self, original):
        --> `self` points to the instance
        --> `original` is the original implementation
    """
    cls, SEL = args

    def decorator(func):
        old_IMP = cls.instanceMethodForSelector_(SEL)

        def wrapper(self, *args, **kwargs):
            return func(self, old_IMP, *args, **kwargs)

        new_IMP = objc.selector(wrapper, selector=old_IMP.selector,
                                signature=old_IMP.signature)
        objc.classAddMethod(cls, SEL, new_IMP)
        return wrapper

    return decorator


@swizzle(objc.lookUpClass('NSBundle'), b'bundleIdentifier')
def swizzled_bundleIdentifier(self, original):
    """Swizzle [NSBundle bundleIdentifier] to make NSUserNotifications
    work.

    To post NSUserNotifications OS X requires the binary to be packaged
    as an application bundle. To circumvent this restriction, as it would
    be difficult (impossible?) to implement in an Alfred Extension,
    we modify `bundleIdentifier` to return a fake bundle identifier.
    """
    # Return Python Launcher's bundle identifier to display the Python Launcher logo.
    
    return 'org.python.PythonLauncher'



########################################################################
#      L'envoi de la noticiation au centre de notification             #
########################################################################

def notify(title, text):
    """Display a NSUserNotification on Mac OS X >= 10.8"""
    NSUserNotification = objc.lookUpClass('NSUserNotification')
    NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
    
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setInformativeText_(text)
    
    NSUserNotificationCenter.defaultUserNotificationCenter().deliverNotification_(notification)







