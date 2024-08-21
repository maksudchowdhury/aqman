# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
client_domain_url="@usbair.com" #change this to the domain of the client
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def custom_context_variables(request):
    return {
        'client_domain':client_domain_url,
    }