---
template: calc.html
extensions: [md_in_html]
---

# Price calculations

Please see our page about [terms and fees](https://www.uu.se/en/centre/uppmax/get-started/terms-and-fees)
for more information about pricing, services and terms. Note that these
calculations do not include the subsidization by the disciplinary domains.

<p>
 <b>Service:</b>
 <input type="radio" id="service_pelle" name="service" value="pelle" checked>
 <label for="service_pelle">Pelle</label>
 <input type="radio" id="service_pelle_cloud" name="service" value="pelle-cloud">
 <label for="service_pelle_cloud">Pelle Cloud</label>
 <input type="radio" id="service_maja" name="service" value="maja">
 <label for="service_maja">Maja</label>
</p>

<table id="ucalc">
 <thead>
  <tr>
   <th><p>Resource:</p></td>
   <th><p>Amount:</p></td>
   <th><p>Price:</p></td>
   <th><p>Total cost (per year):</p></td>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td><label for="cpu">CPU</label></td>
   <td><input type="number" id="cpu"><span class="input-unit"></span></td>
   <td><p class="price"></p></td>
   <td><p class="total"></p></td>
  </tr>
  <tr>
   <td><label for="cpu-highmem">CPU High-memory</label></td>
   <td><input type="number" id="cpu-highmem"><span class="input-unit"></span></td>
   <td><p class="price"></p></td>
   <td><p class="total"></p></td>
  </tr>
  <tr>
   <td><label for="gpu-small">GPU Small</label></td>
   <td><input type="number" id="gpu-small"><span class="input-unit"></span></td>
   <td><p class="price"></p></td>
   <td><p class="total"></p></td>
  </tr>
  <tr>
   <td><label for="gpu-medium">GPU Medium</label></td>
   <td><input type="number" id="gpu-medium"><span class="input-unit"></span></td>
   <td><p class="price"></p></td>
   <td><p class="total"></p></td>
  </tr>
  <tr>
   <td><label for="gpu-large">GPU Large</label></td>
   <td><input type="number" id="gpu-large"><span class="input-unit"></span></td>
   <td><p class="price"></p></td>
   <td><p class="total"></p></td>
  </tr>
  <tr>
   <td><label for="proj-storage">Project storage</label></td>
   <td><input type="number" id="proj-storage"><span class="input-unit"></span></td>
   <td><p class="price"></p></td>
   <td><p class="total"></p></td>
  </tr>
 </tbody>
 <tfoot>
  <tr>
   <td colspan="3"><strong>Sum:</strong></td>
   <td><p><strong id="price-sum"></strong></b></td>
  </tr>
 </foot>
</table>
