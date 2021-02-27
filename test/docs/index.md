Welcome to {{ customer.web_url }}

Where we should see junk.a_key: {{ junk.a_key }}

Which can also be written as junk['a_key']: {{junk['a_key']}} 

Or even extra['junk']['a_key']: {{extra['junk']['a_key']}}

Use `extra` to call a file which violates Python variable naming rules.

For example, if the file starts with a number: {{extra['1_foo']['bar']}}

Inside the included md file there 3 {{ star }}

<!-- throws TemplateSyntaxError('Missing end of comment tag') unless comment_start_string is configured -->
You can use `{#binding.path}` to update the UI when the model changes.
