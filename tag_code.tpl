{% extends 'full.tpl'%}

{%- macro random_int(len) -%}
  {%- for _ in range(len) -%}
    {{ range(10) | random }}
  {%- endfor -%}
{%- endmacro -%}

{%- macro unique_id(group_len=10, separator='') -%}
  {%- set parts -%}
      {{ random_int(group_len) }}
  {%- endset -%}
  {{ parts|join(separator) }}
{%- endmacro -%}

{% block html_head %}
<style>
.prompt.output_prompt {
    color: white;
}
.prompt.input_prompt {
    color: white;
}
</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
</script>
    {{ super() }}
{% endblock html_head %}

{% block body %}
    {{ super() }}
{% endblock body %}

{% block codecell %}
    {{ super() }}
{% endblock codecell %}

{% block output_area_prompt %}
{{ super() }}
{% endblock output_area_prompt %}

{% block in_prompt %}
{{ super() }}
{% endblock in_prompt %}


{% block input_group %}
{%- set id = unique_id() -%}

<div id="container-fluid">
    <div class="row">
      <div class="col-2">
      <button type="button" class="btn btn-primary btn-xs" data-toggle="collapse" data-target="#{{id}}" style="">Show Code</button>
      </div>
    </div>
  </div>

<div id={{id}} class ="collapse">
    </br>
    {{ super() }}
</div>

{% endblock input_group %}
